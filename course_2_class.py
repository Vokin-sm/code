class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError(str(x) + " is negative number")


a = PositiveList([1, 2, 3])
a.append(-1)
print(a)
