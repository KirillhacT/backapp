number = 12312312443

for i in range(1, int(number ** 0.5) + 1):
    for j in range(1, int(number ** 0.5) + 1):
        if i ** j == number:
            print(f"{i}, {j}")
