"""2024–2025 Scouting TX Calc Program"""
import time
from math import pi, sin
import matplotlib.pyplot as plt
import colorama
import progressbar_


# IGNORE THESE VARIABLES
# x = Total Block time
# y = NO. of Blocks
# a = opponent 1 score time
# b = opponent 2 score time
# s = Our sample score time
# α = Our specimen score time
# θ = Teamate score time
# c = Single block duration
# w = win margin
# k = NO. of buckets scored
# r = NO. of specimen scored
# t = match time passed
# m = total NO. of times
# g = block gap time
# u = 1, -1 (m)

# _s = sample
# _p = points
# _se = sec
# _p = positions

# uppercase = opp
# lowercase = team

# a = opp1
# b = opp2

# Set all vars to zero
# todo: add input statement


# Equations

def u(t, n, l, isblocked):
    """

    :param t:
    :param n:
    :param l:
    :param isblocked:
    :return:
    """
    global output_calculated
    if not isblocked:
        output_calculated = 1 * sin((pi / n) * t + l)
    
    elif isblocked:
        output_calculated = sin((pi / n) * t)
    
    return output_calculated


def calcloop(depth, current, tree, r_t, r_n, r_l):
    """

    :param depth:
    :param current:
    :param tree:
    :param r_t:
    :param r_n:
    :param r_l:
    """
    if current <= depth:
        tree_true = u(r_t, r_n, r_l, True)
        
        tree.append([tree_true, current, True])
        calcloop(depth, current + 1, tree, r_t, r_n, r_l)
        
        tree_false = u(r_t, r_n, r_l, False)
        
        tree.append([tree_false, current, False])
        calcloop(depth, current + 1, tree, r_t, r_n, r_l)
    
    
    
    else:
        pass


def iter_calcloop(depth: int, calc_n: int, calc_l: float, start: int, team: int = 0):
    """

    :param depth:
    :param calc_n:
    :param calc_l:
    :param start:
    :param team:
    :return:
    """
    global pavgcol
    tree = []
    txtree = [0]
    prv = 1
    prv1 = 1
    prv2 = 1
    prv3 = 1
    pavg = 1
    
    for i in range(120 - start):
        
        st1 = time.time_ns()
        #print(f"\rGenerating Tree {i}, prev: {round(prv, 2)} ms", end="")
        if prv1 > prv:
            pmincol = colorama.Fore.GREEN
        elif prv1 < prv:
            pmincol = colorama.Fore.RED
        else:
            pmincol = colorama.Fore.YELLOW
        
        pavg = round(pavg, 2)
        
        if pavg > 5000:
            pavgcol = colorama.Fore.RED
        if 1000 < pavg < 4999:
            pavgcol = colorama.Fore.LIGHTRED_EX
        if 500 < pavg < 999:
            pavgcol = colorama.Fore.YELLOW
        if 100 < pavg < 499:
            pavgcol = colorama.Fore.GREEN
        if 0 < pavg < 99:
            pavgcol = colorama.Fore.BLUE
        progressbar_.bar(i, 120 - start, length=15, fill="#",
                         prefix=f"{colorama.Fore.LIGHTWHITE_EX}Generating "
                                f"{120 - start} Trees @ T{team}",
                         suffix=f"{colorama.Fore.LIGHTWHITE_EX}| Tree{i} | "
                                f"Tree Prev Gen Tx: {pmincol}{prv}"
                                f"{colorama.Fore.LIGHTWHITE_EX} | Avg: {pavgcol}{pavg}")
        subtree = []
        
        calcloop(depth, 0, subtree, i, calc_n, calc_l)
        tree.append([f"tree{i}", subtree])
        txtree.append(i)
        prv4 = prv3
        
        prv3 = prv2
        
        prv2 = prv1
        
        prv1 = prv
        
        prv = time.time_ns() - st1
        prv /= 1000000
        prv = round(prv, 2)
        
        pavg = (prv + prv1 + prv2 + prv3 + prv4) / 5
    
    #print(tree)
    print("\n")
    
    #print("\nCalculation Complete")
    return tree, txtree


def find_best(depth, t, n, l, plot, col, team):
    """

    :param depth:
    :param t:
    :param n:
    :param l:
    :param plot:
    :param col:
    :param team:
    """
    # this func is incomplete
    plotlist = [0]
    txtree = [0]
    valuetree, timetree = iter_calcloop(depth, n, l, t, team)
    for list in valuetree:
        avgvar = 0
        for list_2 in list[1][0]:
            avgvar += list_2
        
        plotlist.append(list[1][0][0])
    #print(avgvar)
    txtree.append(timetree)
    plot.plot(timetree, plotlist, col)
    
    #print(timetree)


#c_t = int(input("c: "))6
#c_n = int(input("n: "))
#c_l = int(input("l: "))
#dpt = int(input("depth: "))
#print(iter_calcloop(10, 6, 0.5, 0))
#with open("outputs.txt", "w") as _f_e_2:
#    _f_e_2.write(str(iter_calcloop(10, 6, 0.5, 0)))

def find_teams(depth, t1_n, t1_l, t2_n, t2_l, t3_n, t3_l, t4_n, t4_l, start):
    """

    :param depth:
    :param t1_n:
    :param t1_l:
    :param t2_n:
    :param t2_l:
    :param t3_n:
    :param t3_l:
    :param t4_n:
    :param t4_l:
    :param start:
    """
    find_best(depth, start, t1_n, t1_l, plt, "g", 1)
    find_best(depth, start, t2_n, t2_l, plt, "b", 2)
    find_best(depth, start, t3_n, t3_l, plt, "r", 3)
    find_best(depth, start, t4_n, t4_l, plt, "y", 4)
    
    #plt.axes.Axes.axhline()
    
    plt.show()


t1n = float(input("Team 1 n: "))
t1l = float(input("Team 1 l: "))
t2n = float(input("Team 2 n: "))
t2l = float(input("Team 2 l: "))
t3n = float(input("Team 3 n: "))
t3l = float(input("Team 3 l: "))
t4n = float(input("Team 4 n: "))
t4l = float(input("Team 4 l: "))
cdepth = int(input("Tree Calculation Depth: "))
startpos = int(input("Start Position (including hang time): "))

find_teams(cdepth, t1n, t1l, t2n, t2l, t3n, t3l, t4n, t4l, startpos)
