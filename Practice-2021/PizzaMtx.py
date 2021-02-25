

class Pizza():
    """docstring for Pizza."""

    def __init__(self, index, ingredients=[], lenn=-1):
        self.idx = index
        if lenn == -1:
            self.num_ingr = len(ingredients)
        else:
            self.num_ingr = lenn
        self.ingr = ingredients

    def __repr__(self):
        return f"{self.__class__.__name__}({self.idx}, {self.ingr})"

class Team():
    """docstring for Team."""

    def __init__(self, people):
        self.people = people
        self.pizzas = []
        self.weight = 1

    def __repr__(self):
        pizzas = "".join("%s, " % repr(x) for x in self.pizzas)
        return f"{self.__class__.__name__}%d(" % self.people + pizzas[:-2] + ")"

    def __str__(self):
        return f"{self.people} " + " ".join("%d" % x.idx for x in self.pizzas)

    #@property
    #def


class CustomMtx(object):
    """docstring for CustomMtx."""

    def __init__(self, Pizza_list = []):
        super(CustomMtx, self).__init__()

        self.y_axis = []
        self.x_axis = []
        aux = []

        idx = 0
        for p in Pizza_list:
            self.x_axis.append([idx, p])
            idx += 1
            aux.extend(p.ingr)

        len_x = len(self.x_axis)
        aux = dict.fromkeys(aux)
        for key in aux.keys():
            aux[key] = [False]*len_x
        for it in range(len_x):
            for ing in self.x_axis[it][1].ingr:
                aux[ing][it] = True

        self.mtx = []
        keys, values = [], []
        for x,y in aux.items():
            keys.append(x)
            values.append(y)

        for idx in range(len(keys)):
            self.y_axis.append([idx, keys[idx], values[idx].count(True)])

        for it in range(len_x):
            self.mtx.append([])
            for i in range(len(self.y_axis)):
                self.mtx[it].append(values[i][it])

    def pop_xl(self, i = []):
        # return pizzas, not PizzaTuple
        i.sort()
        res = []
        for value in range(len(i)):
            res.append(self.x_axis.pop(i[value] - value)[1])
        return res

    # COSTOSO!
    def print(self):
        row_format = "{:>6}" * (len(self.y_axis)+1)
        ingr_list = [(x[1][:2] + '..') if len(x[1]) > 3 else x[1] for x in self.y_axis] #
        ingr_list.insert(0, " ")
        str = row_format.format(*ingr_list) + "\n"
        for x in self.x_axis:
            ingr = self.mtx[x[0]]
            aux = []
            for y in self.y_axis:
                if ingr[y[0]]:
                    aux.append("X")
                else:
                    aux.append(" ")
            row_format = "p{:<6}" + "{:>6}" * len(self.y_axis)
            str = str + row_format.format(x[1].idx, *aux) + "\n"
        return str

    def extend_xaxis_pizzaWeight(self):
        aux = {}
        len_y = len(self.y_axis)
        for x in range(len_y):
            aux[self.y_axis[x][1]] = x

        aux2 = []
        for PizzaTuple in self.x_axis:
            val = 0
            for ing in PizzaTuple[1].ingr:
                if aux[ing] > val:
                    val = aux[ing]
            PizzaTuple.append(self.mtx[PizzaTuple[0]].count(True)*len_y)#+val)
            aux2.append(PizzaTuple)
        self.x_axis = aux2
