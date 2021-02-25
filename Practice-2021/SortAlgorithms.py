import abc

class SortAlgorthm(abc.ABC):
    """Abstract Base class for this module"""

    @staticmethod
    @abc.abstractmethod
    def sort(arr, key = lambda x : x):
        raise TypeError("SortAlgorthm is an abstract class. DO NOT USE!")


# def myFunc(e):
#     return r[2]
# RadixSort.sort(arr, key = myFunc)
class RadixSort(SortAlgorthm):
    """docstring for RadixSort."""
    @staticmethod
    def __countingSort(arr, exp1, key = lambda x : x):

        n = len(arr)

        # The output array elements that will have sorted arr
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = (key(arr[i]) / exp1)
            count[int(index % 10)] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = (key(arr[i]) / exp1)
            output[count[int(index % 10)] - 1] = arr[i]
            count[int(index % 10)] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    @staticmethod
    def sort(arr, key = lambda x : x):
        # Find the maximum number to know number of digits
        max1 = key(max(arr, key=key))

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp > 0:
            RadixSort.__countingSort(arr, exp, key=key)
            exp *= 10

class TimSort(SortAlgorthm):
    """docstring for TimSort."""

    @staticmethod
    def sort(arr, key = lambda x : x):
        # Default algorithm in python
        arr.sort(key = key)
