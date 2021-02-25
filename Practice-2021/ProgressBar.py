# Simplified Version of https://github.com/Robpol86/etaprogress

from collections import deque
from math import sqrt, ceil
import time
NOW = time.time

class ProgressBar(object):

    CHAR_LEFT_BORDER = '['
    CHAR_RIGHT_BORDER = ']'
    CHAR_EMPTY = ' '
    CHAR_FULL = '='
    CHAR_LEADING = '>'
    NOW = time.time
    HEADER = '{percent}  {fraction}'

    def __init__(self, denominator, max_width=80, eta_every=5):
        self.width = max_width
        self._eta = self.ETA(denominator=denominator)
        self.max_width = max_width
        self.eta_every = eta_every
        self.force_done = False
        self._eta_string = '-- s'
        self._eta_count = 1
        self.HEADER = self.HEADER.format(percent='{perc:>8.2f}%',
            fraction='({num:>' + str(len(str(denominator))) + 'd}/{den:d})')

    @property
    def _generate_eta(self, leading_zero=False):
        """Returns a human readable ETA string."""
        seconds = self._eta.eta_seconds
        if not seconds:
            return '-- s'

        # Convert seconds to other units.
        final_days, final_hours, final_minutes, final_seconds = 0, 0, 0, seconds
        if final_seconds >= 86400:
            final_days = int(final_seconds / 86400.0)
            final_seconds -= final_days * 86400
        if final_seconds >= 3600:
            final_hours = int(final_seconds / 3600.0)
            final_seconds -= final_hours * 3600
        if final_seconds >= 60:
            final_minutes = int(final_seconds / 60.0)
            final_seconds -= final_minutes * 60
        final_seconds = int(ceil(final_seconds))

        # Determine which string template to use.
        if final_days:
            template = '{0:d}d {1:d}h' if leading_zero else '{0}d {1}h'
        elif final_hours:
            template = '{1:d}h {2:02d}m {3:02d}s' if leading_zero else '{1}h {2}m {3}s'
        elif final_minutes:
            template = '{2:02d}m {3:02d}s' if leading_zero else '{2}m {3}s'
        else:
            template = '{3:02d}s' if leading_zero else '{3}s'

        return template.format(final_days, final_hours, final_minutes, final_seconds) + ' '*10

    @property
    def denominator(self):
        """Returns the denominator as an integer."""
        return int(self._eta.denominator)

    @property
    def done(self):
        """Returns True if the progress has completed."""
        if self.force_done:
            return True
        return self._eta.done

    @property
    def numerator(self):
        """Returns the numerator as an integer."""
        return int(self._eta.numerator)

    @numerator.setter
    def numerator(self, value):
        """Sets a new numerator and generates the ETA. Must be greater than or equal to previous numerator."""
        # If ETA is every iteration, don't do anything fancy.
        if self.eta_every <= 1:
            #self._eta.numerator = value
            self._eta.set_numerator(value, calculate=True)
            self._eta_string = self._generate_eta
            return

        # If ETA is not every iteration, unstable rate is used. If this bar is undefined, no point in calculating ever.
        if self._eta.undefined:
            self._eta.set_numerator(value, calculate=False)
            return

        # Calculate if this iteration is the right one.
        if self._eta_count >= self.eta_every:
            self._eta_count = 1
            #self._eta.numerator = value
            self._eta.set_numerator(value, calculate=True)
            self._eta_string = self._generate_eta
            return

        self._eta_count += 1
        self._eta.set_numerator(value, calculate=False)

    @property
    def percent(self):
        """Returns the percent as a float."""
        return float(self._eta.percent)

    @property
    def undefined(self):
        """Return True if the progress bar is undefined (unknown denominator)."""
        return self._eta.undefined

    def __str__(self):
        percent = self.percent
        header = self.HEADER.format(perc=percent, num=self.numerator, den=self.denominator)

        width = self.width - (10 + len(header))
        units = int(percent * 0.01 * width) if width > 0 else 0
        bar = (
            self.CHAR_LEFT_BORDER +
            self.CHAR_FULL * (units - 1) +
            (self.CHAR_LEADING if (width-units > 0) else self.CHAR_FULL) +
            self.CHAR_EMPTY * (width - units) +
            self.CHAR_RIGHT_BORDER
        )

        if self.numerator == self.denominator:
            template = '{header} {bar} Done!' + 10*' '
        else:
            template = '{header} {bar} ETA: {eta}'
        return template.format(header=header, bar=bar,
            eta=self._eta_string)

    class ETA(object):
        """
            Calculates the estimated time remaining using Simple Linear Regression.
            If `denominator` is 0 or None, no ETA will be available.
        """
        def __init__(self, denominator=0, scope=60):
            self.denominator = denominator # the final/total number of units. 0 if unknown.
            self.eta_epoch = None
            self.rate = 0.0

            self._start_time = NOW()
            self._timing_data = deque(maxlen=scope)

        @property
        def numerator(self):
            """Returns the latest numerator."""
            return self._timing_data[-1][1] if self._timing_data else 0

        @property
        def started(self):
            """Returns True if there is enough data to calculate the rate."""
            return len(self._timing_data) >= 2

        @property
        def undefined(self):
            """Returns True if there is no denominator."""
            return self.denominator is None or self.denominator <= 0

        @property
        def done(self):
            """Returns True if numerator == denominator."""
            return False if self.undefined else self.numerator == self.denominator

        @property
        def eta_seconds(self):
            """Returns the ETA in seconds or None if there is no data yet."""
            return None if self.eta_epoch is None else max([self.eta_epoch - NOW(), 0])

        @property
        def percent(self):
            """Returns the percent as a float."""
            return 0.0 if self.undefined else self.numerator / self.denominator * 100

        def set_numerator(self, numerator, calculate=True):
            """Sets the new numerator (number of items done).
            Positional arguments:
            numerator -- the new numerator to add to the timing data.
            Keyword arguments:
            calculate -- calculate the ETA and rate by default.
            """
            # Validate
            if self._timing_data and numerator < self._timing_data[-1][1]:
                raise ValueError('numerator cannot decrement.')

            # Update data.
            now = NOW()
            if self._timing_data and now == self._timing_data[-1][0]:
                self._timing_data[-1] = (now, numerator)  # Overwrite.
            else:
                self._timing_data.append((now, numerator))

            # Calculate ETA and rate.
            if not self.done and calculate and self.started:
                self._calculate()

        def _calculate(self):
            """
                Perform the ETA and rate calculation.
                Two linear lines are used to calculate the ETA: the linear regression, and the fitted line.
                As the percentage moves closer to 100%, _calculate() gradually uses the ETA based on the
                fitted line more and more. This is done to prevent an ETA that's in the past.
            """
            # Calculate means and standard deviations.
            mean_x = sum(i[0] for i in self._timing_data) / len(self._timing_data)
            mean_y = sum(i[1] for i in self._timing_data) / len(self._timing_data)
            std_x = sqrt(sum(pow(i[0] - mean_x, 2) for i in self._timing_data) / (len(self._timing_data) - 1))
            std_y = sqrt(sum(pow(i[1] - mean_y, 2) for i in self._timing_data) / (len(self._timing_data) - 1))

            # Calculate coefficient.
            sum_xy, sum_sq_v_x, sum_sq_v_y = 0, 0, 0
            for x, y in self._timing_data:
                x -= mean_x
                y -= mean_y
                sum_xy += x * y
                sum_sq_v_x += pow(x, 2)
                sum_sq_v_y += pow(y, 2)
            pearson_r = sum_xy / sqrt(sum_sq_v_x * sum_sq_v_y)

            # Calculate regression line. y = mx + b where m is the slope and b is the y-intercept.
            m = self.rate = pearson_r * (std_y / std_x)
            if self.undefined:
                return
            y = self.denominator
            b = mean_y - m * mean_x
            x = (y - b) / m

            # Calculate fitted line (transformed/shifted regression line horizontally).
            fitted_b = self._timing_data[-1][1] - (m * self._timing_data[-1][0])
            fitted_x = (y - fitted_b) / m
            adjusted_x = ((fitted_x - x) * (self.numerator / self.denominator)) + x
            self.eta_epoch = adjusted_x
