string = "abcdefd2"
new_str = ""
for i in range(len(string)):
    if i % 2 != 0 and i != len(string) - 1:
        new_str += f"{string[i]} "
    else:
        new_str += string[i]
mas = new_str.split(" ")
if len(mas[-1]) == 1:
    mas[-1] += "_"
print(mas)


