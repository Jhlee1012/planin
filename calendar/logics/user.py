from event import *

class User:

    def __init__(self, name = None):
        self.name = name
        self.events = []

    def add_event(self, event):

        idx = len(self.events)
        for i, e in enumerate(self.events):
            if e.start > event.start:
                idx = i
                break

        self.events.insert(idx, event)


    def __str__(self):
        res = self.name
        for e in self.events:
            res += '\n' + str(e)
        return res
