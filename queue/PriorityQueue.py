from typing import Any


class PriorityQueue(object):
    """
    Data structure for a priority queue. Built on a list data structure
    """

    def __init__(self):
        self.queue = []

    def is_empty(self) -> bool:
        return len(self) == 0

    def add(self, data) -> None:
        self.queue.append(data)
        self.queue = sorted(self.queue)

    def remove(self) -> Any:
        if self.is_empty():
            return
        return self.queue.pop()

    def peek(self) -> Any:
        if self.is_empty():
            return
        return self.queue[-1]

    def __len__(self):
        return len(self.queue)
