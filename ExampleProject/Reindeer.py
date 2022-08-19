class Reindeer:
    """
    Class to represent a Reindeer
    """
    def __init__(self, name="No name set"):
        """
        Create member data for a reindeer
        :param name: The reindeer's name
        """
        self.name = name
        self.clean = False
        self.trimmed = False

    def __str__(self):
        return f"{self.name} is clean: {self.clean} and is trimmed: {self.trimmed}"
