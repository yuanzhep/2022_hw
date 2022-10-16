"""
CSC645 HW 1.2
By: yuanzhe peng
"""

from __future__ import print_function
import random 

dust = [random.randint(0,1),random.randint(0,1)]
position_V = random.randint(0,1)
location_V = [("V"," "),(" ","V")]
action =('Finish','Right','Left','Suck')
k = 0

def print_v():
    print("Environment")
    print('Position   A  ', ' B  ')
    print('Dirty  ',*dust, sep = "    ")
    print('pos_vac', *location_V[position_V], sep = "    ")

def agent_v():
    if dust[position_V] == 1:
        dust[position_V] = 0
        n = 3
    elif dust[position_V] == 0 and position_V == 0 and dust[1-position_V] == 1:
        n = 1
    elif dust[position_V] == 0 and position_V == 1 and dust[1-position_V] == 1:
        n = 2
    elif dust[0] == 0 and dust[1] == 0:
        n = 0
    return n

print_v()
while k > -2:
    x = agent_v()
    if x != 3:
         position_V = 1 - position_V
    else:
        k += 2
    k -= 1
    print_v()   
    print('Status: ',action[x])
