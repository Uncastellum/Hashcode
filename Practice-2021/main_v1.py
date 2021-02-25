import os, sys, time
from random import shuffle, randint
from PizzaMtx import *
from SortAlgorithms import *
from ProgressBar import ProgressBar

files = [
    'a_example.in',
    'b_little_bit_of_everything.in',
    'c_many_ingredients.in',
    'd_many_pizzas.in',
    'e_many_teams.in'
]

args = sys.argv[1:]
index = 0
if len(args) != 0:
    file = args[0]
    if file in ['a', 'b', 'c', 'd', 'e']:
        index = ['a', 'b', 'c', 'd', 'e'].index(file)
    elif path in ['1', '2', '3', '4', '5']:
        index = ['1', '2', '3', '4', '5'].index(file)

input = 'input/' + files[index]
output_file = 'output_' + ['a', 'b', 'c', 'd', 'e'][index] + '.out'

with open(input) as f_in:
    # read first line
    pizzas, two_pp_team, tree_pp_team, four_pp_team = [int(x) for x in next(f_in).split()]
    matrix = []
    index = 0
    for line in f_in: # read rest of lines
        parsed = [x for x in line.split()]
        matrix.append(Pizza(index, ingredients=parsed[1:], lenn=int(parsed[0])))
        index += 1
    # Teams:
    if two_pp_team%2 > 1:
        teams = [Team(2) for x in range(two_pp_team-1)]
    else:
        teams = [Team(2) for x in range(two_pp_team)]

    teams.extend([Team(3) for x in range(tree_pp_team)])
    teams.extend([Team(4) for x in range(four_pp_team)])
    shuffle(teams)
    teams = [teams, []]

def resulttofile(res):
    with open(output_file, 'w') as f_out:
        f_out.write(str(len(res)))
        f_out.write("\n")
        for item in res:
            f_out.write(str(item))
            f_out.write("\n")

def get_idx_aprox(list1, elem):
    for i in range(len(list1)):
        if elem < list1[i]:
            return i
    return 0

def or_l(l1, l2):
    res = []
    for i in range(len(l1)):
        if l1[i] or l2[i]:
            res.append(True)
        else:
            res.append(False)
    return res

hist = [0,0,0,0]
def clear_s():
    hist = [0,0,0,0]
def corta(rest, tot, p_l, bo_l, bo_idx):
    if tot < 5000 or rest < 2000:
        return False
    if rest % 500 != 0:
        return False
    if hist.count(bo_idx) != 4:
        return False
    hist.pop(0)
    hist.append(bo_idx)
    # soft sol?
    return True


def match(cm, restrictive = 0.8):
    l_y = len(cm.y_axis)
    pb = ProgressBar(len(cm.x_axis), eta_every=5)
    for a in range(len(teams[0])):
        l_x = len(cm.x_axis)
        team = teams[0].pop(0)
        if l_x == 0:
            teams[0].append(team)
            print('')
            return False
        if l_x < team.people:
            teams[0].append(team)
            continue

        sa1,sa2,sa3 = None, None, None

        p1 = l_x-1
        pizza = cm.x_axis[p1]

        sa1 = 0
        best_opt = cm.x_axis[0]
        best_opt_or = or_l(cm.mtx[best_opt[0]], cm.mtx[pizza[0]])
        it = 0
        clear_s()
        for i in cm.x_axis:
            if corta(it, l_x, cm.mtx[pizza[0]], best_opt_or, sa1):
                break
            if best_opt_or.count(True) > l_y*restrictive*0.8:
                break
            buc_aux = or_l(cm.mtx[i[0]], cm.mtx[pizza[0]])
            if buc_aux.count(True) > best_opt_or.count(True):
                sa1 = it
                best_opt_or = buc_aux
                best_opt = i
            it += 1

        if team.people != 2:
            union = best_opt_or
            it = 0
            clear_s()
            if 0 in [p1,sa1]:
                sa2 = 1
                best_opt = cm.x_axis[1]
            else:
                sa2 = 0
                best_opt = cm.x_axis[0]
            for i in cm.x_axis:
                if corta(it, l_x, union, best_opt_or, sa2):
                    break
                if it in [p1, sa1]:
                    it += 1
                    continue
                if best_opt_or.count(True) > l_y*restrictive*0.9:
                    break
                buc_aux = or_l(cm.mtx[i[0]], union)
                if buc_aux.count(True) > best_opt_or.count(True):
                    sa2 = it
                    best_opt_or = buc_aux
                    best_opt = i
                it += 1

            if team.people != 3:
                union = best_opt_or
                it = 0
                clear_s()
                if 0 in [p1,sa1,sa2]:
                    if 1 in [p1,sa1,sa2]:
                        sa3 = 2
                        best_opt = cm.x_axis[2]
                    else:
                        sa3 = 1
                        best_opt = cm.x_axis[1]
                else:
                    sa3 = 0
                    best_opt = cm.x_axis[0]
                best_opt = cm.x_axis[0]
                for i in cm.x_axis:
                    if corta(it, l_x, union, best_opt_or, sa3):
                        break
                    if it in [p1, sa1, sa2]:
                        if not p1>it:
                            it += 1
                        continue
                    if best_opt_or.count(True) > l_y*restrictive:
                        break
                    buc_aux = or_l(cm.mtx[i[0]], union)
                    if buc_aux.count(True) > best_opt_or.count(True):
                        sa3 = it
                        best_opt_or = buc_aux
                        best_opt = i
                    it += 1

        popper = [x for x in [p1,sa1,sa2,sa3] if x is not None]
        pb.numerator +=  len(popper)
        print("{:>4}".format(restrictive) + str(pb), end='\r')
        team.pizzas = cm.pop_xl(popper)
        teams[1].append(team)
    print('')
    if len(teams[0]) == 0:
        return False
    if len(cm.x_axis) < min(teams[0], key=lambda x: x.people).people:
        return False
    return True

def main():
    tim = time.process_time()
    print("Building Matrix... ", end ='\r')
    cm = CustomMtx(Pizza_list = matrix)
    print("Building Matrix... OK (%.2fs)" % (time.process_time() - tim))

    tim = time.process_time()
    print("Sorting y-axis... ", end ='\r')
    RadixSort.sort(cm.y_axis, key=lambda x: x[2])
    print("Sorting y-axis... OK (%.2fs)" % (time.process_time() - tim))

    tim = time.process_time()
    print("Extending & Sorting x-axis... ", end ='\r')
    cm.extend_xaxis_pizzaWeight()
    RadixSort.sort(cm.x_axis, key=lambda x: x[2])
    print("Extending & Sorting x-axis... OK (%.2fs)" % (time.process_time() - tim))

    #print(cm.print())

    for r in [0.8, 0.5, 0.25, 0]:
        cntinue = match(cm,restrictive=r)
        if not cntinue:
            break

    print("%d pizzas assigned." % (pizzas - len(cm.x_axis)))
    resulttofile(teams[1])
    #print(cm.print()) # #print(cm.y_axis)


if __name__ == '__main__':
    main()
