class Pet:
    """
    Basic class to provide pet functionality.
    Is the parent class of Dog and Tiger
    """

    def __init__(self, name=None, weight=None):
        if weight < 0:
            raise Exception(f"Tried to apply a weight of {weight} to pet {name} in {__name__}!")

        self.name = name
        self.weight = weight

    def feed(self, feed_amount=0):
        if feed_amount < 0:
            raise Exception(f"Tried to feed pet {self.name} in {__name__} a negative amount of food!")

        self.weight += feed_amount

    def walk(self):
        weight_reduction = 0.05 * self.weight
        self.weight -= weight_reduction

        if self.weight <= 0:
            raise Exception(f"Walking {self.name} resulted in a weight below zero in {__name__}")

    def __str__(self):
        return f"{self.name} has a weight of {self.weight:.2f}"


class Dog(Pet):
    """
    A simple class which inherits the Pet class and adds functionality, like a bark function
    as well as a custom walk function.
    """

    def __init__(self, name=None, weight=None):
        super(Dog, self).__init__(name, weight)

    def walk(self):
        """
        Use the function used to approximate e to calculate the weight lost when the dog is walked
        :return:
        """
        weight_div = (self.weight / 50)
        self.weight -= -(1 / (weight_div - 1) + 1)

    @staticmethod
    def bark():
        print("Bark! Bark!")

    def __str__(self):
        return super(Dog, self).__str__() + " and is a very good boy!"


class Tiger(Pet):
    """
    A simple class which inherits the Pet class and adds functionality, like a roar function as well as a custom walk
    function
    """
    def __init__(self, name=None, weight=None):
        super(Tiger, self).__init__(name, weight)

    def walk(self):
        self.weight -= (self.weight * 0.1)

        if self.weight <= 0:
            raise Exception(f"Walking {self.name} resulted in a weight below zero in {__name__}")

    @staticmethod
    def roar():
        print("Roar!")

    def __str__(self):
        return super(Tiger, self).__str__()+" and is very scary!"


