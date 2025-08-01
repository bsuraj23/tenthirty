class Countupto:
    def __init__(self, max):
        self.max=max
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.max:
            num
