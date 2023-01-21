class Mas:
    def __init__(self):
        self.mas = [1, 2, 3]
        self.indicator = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indicator >= len(self.mas):
            raise StopIteration()
        current = self.mas[self.indicator]
        self.indicator += 1
        return current

a = Mas()