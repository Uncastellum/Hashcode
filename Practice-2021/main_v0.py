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

def match(cm, l_cascade, restrictive = 0.8):
    l_y = len(cm.y_axis)
    pb = ProgressBar(len(cm.x_axis), eta_every=5)
    for a in range(len(teams[0])):
        l_x = len(cm.x_axis)
        team = teams[0].pop(0)
        if l_x == 0:
            teams[0].append(team)
            print('')
            return False, l_cascade
        if l_x < team.people:
            teams[0].append(team)
            continue

        sa1,sa2,sa3 = None, None, None

        if team.people == 2:
            p1, sa1 = 0, -1
        elif team.people == 3:
            p1, sa1, sa2 = 0, -1, 1
        else:
            p1, sa1, sa2, sa3 = 0, -1, 1, -2

        popper = [x for x in [p1,sa1,sa2,sa3] if x is not None]
        pb.numerator +=  len(popper)
        print("{:>4}".format(restrictive) + str(pb), end='\r')
        team.pizzas = cm.pop_xl(popper)
        teams[1].append(team)
    print('')
    if len(teams[0]) == 0:
        return False, l_cascade
    if len(cm.x_axis) < min(teams[0], key=lambda x: x.people).people:
        return False, l_cascade
    return True, l_cascade

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
    len_y = len(cm.y_axis)
    limit_mtx = [0]
    for idx in range(len(cm.x_axis)):
        if idx != limit_mtx[-1]:
            if cm.x_axis[idx][2]//len_y != cm.x_axis[limit_mtx[-1]][2]//len_y:
                limit_mtx.append(idx)

    for r in [0.8, 0.5, 0.25, 0]:
        cntinue, limit_mtx = match(cm, limit_mtx, restrictive=r)
        if not cntinue:
            break

    print("%d pizzas assigned." % (pizzas - len(cm.x_axis)))
    resulttofile(teams[1])
    #print(cm.print()) # #print(cm.y_axis)


if __name__ == '__main__':
    main()
