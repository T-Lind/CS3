from queue import PriorityQueue
PriorityQueue = PriorityQueue.PriorityQueue
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        if other.age > self.age:
            return True
        return False

    def __gt__(self, other):
        if other.age > self.age:
            return True
        return False

myQueue = PriorityQueue()
myQueue.add(Dog("Fluffy", 10))
myQueue.add(Dog("Fido", 18))
print(myQueue.remove())
