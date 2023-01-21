num1 = 201455
num2 = 201470

for i in range(num1, num2 + 1):
    d = 0
    mas = []
    for j in range(1, i+1):
        if d > 4:
            break
        if i % j == 0:
            mas.append(j)
            d += 1
    if d == 4:
        print(i, mas)
