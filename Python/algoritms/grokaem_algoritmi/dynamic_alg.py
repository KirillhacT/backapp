str1 = "fish"
str2 = "hish"

# dict = {0: {0: "1", 1:"1"}, 1:{0:"1", 1:"1"}}
# for i in str1:
#     for j in range(len(str2)):
#         if str1[i] == str2[j]:
#             dict[i][j] = dict[i-1][j-1] + 1
#         else:
#             dict[i][j] = 0
# print(dict)
# print(dict["talk"]["egor"])


#Заполнение словаря
# dict = {}
# for i in range(len(str1)):
#     dict[i] = {}
#     for j in range(len(str2)):
#         dict[i][j] = 0
# print(dict)

dict = {}
key = 0
for i in str1:
    dict[i] = {}
    for j in str2:
        if i == j:
            key += 1
            dict[i][j] = key
        else:
            dict[i][j] = 0
print(dict)

