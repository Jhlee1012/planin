from datetime import *

class Event:
    def __init__(self, start, end, name = None):
        self.start = start
        self.end = end
        self.name = name

    def collapse(self, other, tolerant = False):
        if tolerant: return not(other.end < self.start or other.start > self.end)
        else: return not(other.end <= self.start or other.start >= self.end)

    def copy(self, name = None):
        if name == None: name = self.name
        return Event(self.start, self.end, name)
        

    def __str__(self):
        return f'{self.name}: {self.start} ~ {self.end}'
