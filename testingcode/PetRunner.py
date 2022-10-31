from Pets import Pet, Tiger, Dog

# First test out regular pet functionality - uses keyword arguments
print("\nPET FUNCTIONALITY:\n")

fluffy = Pet(name="Fluffy", weight=30)
print(fluffy)

fluffy.feed(5)
print(fluffy)

fluffy.walk()
print(fluffy)


# Next, test out the dog child class
print("\nDOG FUNCTIONALITY:\n")

fifo = Dog(name="Fifo", weight=20, happiness="very happy")
print(fifo)

fifo.feed(feed_amount=10)
print(fifo)

fifo.walk()
print(fifo)

fifo.bark()

# Finally, test out the tiger child class
print("\nTIGER FUNCTIONALITY:\n")

bob = Tiger(name="Bob", weight=680, scariness="extremely scary")
print(bob)

bob.feed(feed_amount=50)
print(bob)

bob.walk()
print(bob)

bob.roar()
