s = input()
s1 = "".join([s[i] for i in range(len(s)) if i % 2 != 0])
print(s1)

