class DoubleElement:
    def __init__(self, *lst):
        self.lst = lst
        self.totalIndex = 0

    def __next__(self):

        if self.totalIndex < len(self.lst):
            value_first = self.lst[self.totalIndex]
            if self.totalIndex + 1 >= len(self.lst):
                value_second = None
            else:
                value_second = self.lst[self.totalIndex+1]
            self.totalIndex += 2
            return [value_first,value_second]
        else:
            raise StopIteration

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
