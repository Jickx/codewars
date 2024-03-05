class add(int):
    def __call__(self, value):
        result = self + value
        return add(result)


assert add(1) == 1
assert add(1)(2) == 3
assert add(1)(2)(3) == 6
