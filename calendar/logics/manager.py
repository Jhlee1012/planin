from datetime import *
from event import *
from user import *
from tools import *

user_a = User('강아지')
user_a.add_event(Event(datetime(2022, 1, 1, 9), datetime(2022, 1, 1, 10), 'a'))
user_a.add_event(Event(datetime(2022, 1, 1, 11), datetime(2022, 1, 1, 13), 'c'))

user_b = User('나비')
user_b.add_event(Event(datetime(2022, 1, 1, 9), datetime(2022, 1, 1, 9, 30), 'a'))
user_b.add_event(Event(datetime(2022, 1, 1, 9, 50), datetime(2022, 1, 1, 14), 'b'))


for e in Tools.intersect(user_a.events, user_b.events):
    print(e)
