class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.size() == 0

    def add(self, data):
        self.queue.append(data)
        self.queue = sorted(self.queue)

    def remove(self):
        if self.is_empty(): return
        return self.queue.pop()

    def peek(self):
        if self.is_empty(): return
        return self.queue[-1]

    def size(self):
        return len(self.queue)



if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.add(12)
    myQueue.add(1)
    myQueue.add(14)
    myQueue.add(7)
    print(myQueue)
    while not myQueue.is_empty():
        print(myQueue.remove())
