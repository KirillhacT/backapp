string = "CamelCase"

new_string = ""
for i in range(len(string)):
    current = string[i]
    # if current.lower() != current:
    if current.isupper():
        new_string += f" {current}"
    else:
        new_string += current
print(new_string)