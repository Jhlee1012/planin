from asyncio import events
from datetime import *
from unittest import result
from event import *
from tools import *

class Tools:
    def merge(events):

        if len(events) < 2: return
        current = events[0]
        idx = 1

        for _ in range(1, len(events)):
            target = events[idx]

            if current.collapse(target, True):
                current.end = target.end
                events.remove(target)
            else:
                current = target
                idx += 1


    def reverse(events_in, start, end):
        if len(events_in) == 0: return [Event(start, end)]

        events = []
        results = []
        for e in events_in: events.append(e.copy())
        Tools.merge(events)


        if start < events[0].start: results.append(Event(start, events[0].start))
        for i in range(len(events) - 1): results.append(Event(events[i].end, events[i + 1].start))
        if end > events[-1].end: results.append(Event(events[-1].end, end))

        return results


    def intersect(events_a, events_b):
        results = []

        for current in events_a:
            for target in events_b:
                if current.collapse(target):
                    if current.start > target.start: start = current.start
                    else: start = target.start

                    if current.end > target.end: end = target.end
                    else: end = current.end

                    results.append(Event(start, end))

        return results
