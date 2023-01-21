with open("test2.txt", "r") as file:
    data = file.read()

clear_data = list(map(int, data.split("\n")))
N = clear_data[0]
# print(clear_data)
# print(N)

# N = int(input())
# mas = [N] + [int(input()) for i in range(N)]
# print(mas)

count = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        num1 = clear_data[i]
        num2 = clear_data[j]
        # print(num1, num2)
        sum = num1 + num2
        s = sum % 80 == 0
        if s and (num1 > 50 or num2 > 50):
            count += 1
print(count)