from Reindeer import Reindeer
from ReindeerSpaSupport import *


@debug
@CountCalls
class Trainer:
    def __init__(self, name="No name set"):
        self.name = name

        self.reindeer_assigned = {}

    def add_reindeer(self, reindeer: Reindeer):
        self.reindeer_assigned[reindeer.name] = reindeer

    def remove_reindeer(self, name=None):
        if name is None:
            raise TypeError("You must specify a name to remove a reindeer")

        self.reindeer_assigned.pop(name)

    def get_reindeer(self, name=None):
        if name is None:
            raise TypeError("You must specify a name to get a reindeer")

        return self.reindeer_assigned[name]

    def __str__(self):
        ret = f"{self.name}'s reindeer:\n-----------------\n"
        for key in self.reindeer_assigned:
            ret += key+"\n"

        return ret
