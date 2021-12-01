from random import randint

class Die():
    """A class representing a single die."""

    def __init__(self, num_sides = 6):
        """Assume a 6 sided die"""
        self.num_sides = num_sides

    def describe_die(self):
        """Prints the number of sides of the die"""
        print("The number of sides on this die is: " + str(self.num_sides))
    def roll(self):
        """Return a random number value between 1 and number of sides"""
        return randint(1,self.num_sides) #randint includes the last value no need for a +1
