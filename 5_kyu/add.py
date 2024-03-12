class add(int):
    def __call__(self, value):
        result = self + value
        return add(result)
