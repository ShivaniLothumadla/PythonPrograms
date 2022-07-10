class example:
    def __init__(self, n):
        self.i = 4
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
ex = example(10)
print(list(ex))
