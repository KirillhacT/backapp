value = 153

ex = sum([int(i)**len(str(value)) for i in str(value)]) == value
print(ex)

