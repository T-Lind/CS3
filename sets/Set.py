class IllegalStateWarning(Warning):
    def __init__(self, message, value):
        self.message = message
        self.value = value


class Set:
    def __init__(self, *args):
        self.data = self.__remove_repetition(args)

    def __remove_repetition(self, input):
        repetition_removed = []
        for item in input:
            if repetition_removed.count(item) == 0:
                repetition_removed.append(item)
            else:
                pass
                # raise IllegalStateWarning(f"Tried to input repeated data in {__name__}", item)
        return repetition_removed

    def union(self, other):
        return Set(self.__remove_repetition(self.data+other.data))

    def intersection(self, other):
        intersected_data = []
        for item in self.data:
            if other.data.count(item) != 0:
                intersected_data.append(item)
        return Set(self.__remove_repetition(intersected_data))

    def difference(self, other):
        difference_data = []
        for item in self.data:
            if other.data.count(item) == 0:
                difference_data.append(item)
        return Set(self.__remove_repetition(difference_data))

    def symmetric_difference(self, other):
        difference_data = []
        for item in self.data:
            if other.data.data.count(item) == 0:
                difference_data.append(item)
        for item in other.data:
            if self.data.count(item) == 0:
                difference_data.append(item)
        return Set(self.__remove_repetition(difference_data))

    def __str__(self):
        return str(self.data)
