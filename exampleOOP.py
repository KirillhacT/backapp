class NewClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magic(self):
        return self.x + self.y

a = NewClass(10, 5)
print(a.magic())


