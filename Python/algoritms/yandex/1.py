#Самый частовстречающийся символ в строке
s = input()
# print(max(map(lambda x: (s.count(x), x), s))[1])

# max_element = ""
# max_value = 0
# for i in range(len(s)):
#     current_value = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             current_value += 1
#     if current_value > max_value:
#         max_element = s[i]
#         max_value = current_value
# print(max_element)

hash = {}
for i in s:
    if i not in hash:
        hash[i] = 1
    else:
        hash[i] += 1
print(hash)
max = 0
el = ""
for i in hash:
    if hash[i] > max:
        max = hash[i]
        el = i
print(el)

max_element = ""
max_value = 0
for now in set(s):
    current_value = 0
    for j in range(len(s)):
        if now == s[j]:
            current_value += 1
    if current_value > max_value:
        max_element = now
        max_value = current_value
print(max_element)