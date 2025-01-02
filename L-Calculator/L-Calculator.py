"2024–2025 Scouting TX Calc Program"
import time

from math import *
import matplotlib.pyplot as plt
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

def u(t, n, l, isBlocked):
    if not isBlocked:
        output_calculated = 1 * sin((pi/n)*t + l)
        
    elif isBlocked:
        output_calculated = sin((pi/n)*t)

    return output_calculated




def calcloop(depth, current, tree, r_t, r_n, r_l):
    

    if current <= depth:
        tree_true = u(r_t, r_n, r_l, True)
        
        tree.append([tree_true, current, True])
        calcloop(depth, current + 1, tree, r_t, r_n, r_l)
    
    
        tree_false = u(r_t, r_n, r_l, False)
        
        tree.append([tree_false, current, False])
        calcloop(depth, current + 1, tree, r_t, r_n, r_l)
    
    
    
    else:
        pass



def iter_calcloop(depth, calc_n, calc_l, start):
    tree = []
    txtree = []
    txtree.append(0)
    prv = 0
    
    for i in range(120-start):
        
        st1 = time.time_ns()
        print(f"\rGenerating Tree {i}, prev: {round(prv, 2)} ms", end="")
        subtree=[]
        
        calcloop(depth, 0, subtree, i, calc_n, calc_l)
        tree.append([f"tree{i}", subtree])
        txtree.append(i)
        prv = time.time_ns() - st1
        prv = prv/1000000
        
    print(tree)
    
    print("\nCalculation Complete")
    return tree, txtree

    



def find_best(depth, t, n, l, plt, col):
    # this func is incomplete
    plotlist = [0]
    txtree=[0]
    valuetree, timetree = iter_calcloop(depth, n, l, t)
    for list in valuetree:
        avgvar = 0
        for list_2 in list[1][0]:
            avgvar += list_2
        
        plotlist.append(list[1][0][0])
        print(avgvar)
    pass
    txtree.append(timetree)
    plt.plot(timetree, plotlist, col)
    
    print("")
    #print(timetree)

#c_t = int(input("c: "))6
#c_n = int(input("n: "))
#c_l = int(input("l: "))
#dpt = int(input("depth: "))
#print(iter_calcloop(10, 6, 0.5, 0))
#with open("outputs.txt", "w") as _f_e_2:
#    _f_e_2.write(str(iter_calcloop(10, 6, 0.5, 0)))

def findTeams(depth, t1_n, t1_l, t2_n, t2_l, t3_n, t3_l, t4_n, t4_l):
    
    find_best(depth, 0, t1_n, t1_l, plt, "g")
    find_best(depth, 0, t2_n, t2_l, plt, "b")
    find_best(depth, 0, t3_n, t3_l, plt, "r")
    find_best(depth, 0, t4_n, t4_l, plt, "y")
    
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

findTeams(cdepth, t1n, t1l, t2n, t2l, t3n, t3l, t4n, t4l)