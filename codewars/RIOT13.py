alphavit = "abcdefghijklmnopqrstuvwxyz"
N = len(alphavit)
T = 13
string = "Test!"

def get_index(value):
    return alphavit.index(value)

new_str = ""
for i, j in enumerate(string):
    if j.isupper():
        index = (get_index(j.lower()) + T) % N
        new_str += alphavit[index].upper()
    elif j.islower():
        index = (get_index(j) + T) % N
        new_str += alphavit[index]
    else:
        new_str += j
print(new_str)
