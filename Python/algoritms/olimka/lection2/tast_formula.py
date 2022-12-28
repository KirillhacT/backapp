#1
# N = int(input())

# N1 = N // 48
# N %= 48
# N2 = N // 16
# N %= 16
# N3 = N // 4
# N %= 4
# print(N1, N2, N3, N)


#2 1 
# K = int(input())
# N = int(input())
# str = 0
# a = 1
# while True:
#     str += a
#     if K > N:
#         b = N % K
#         print(str, b)
#         break
#     else:
#         a = N // K
#         N %= K

#2 2
K = int(input())
N = int(input())

str = (N + K - 1) // K
num_str = N % K
print(str, num_str)

#3
text = input()
N = int(input())
dict = {}
for i in range(N):
    dict[i] = input()

str = ""
for i in range(len(text)):
    str += text[i]
    if str in list(dict.values()):
        print(str, end=" ")
        str = ""



