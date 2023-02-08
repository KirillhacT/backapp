a = [1,1,3,3,7,2,2,2,2]
b = 1
c = []
hash = {}
for i in a:
    if i not in hash:
        c.append(i)
        hash[i] = 1
    else:
        hash[i] += 1
        if hash[i] <= b:
            c.append(i)
print(c)

