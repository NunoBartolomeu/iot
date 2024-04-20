from Message import Message
from datetime import datetime

class Limit:
    def __init__(self, name, ideal, min_value, max_value, warn_at_diff):
        self.name = name
        self.ideal = ideal
        self.min = min_value
        self.max = max_value
        self.warn_at_diff = warn_at_diff

    def produce_message(self, value):
        diff = round(value - self.ideal, 2)
        if diff > self.max + self.warn_at_diff or diff < self.min - self.warn_at_diff:
            state = 'Action'
        elif diff > self.max or diff < self.min:
            state = 'Warning'
        else:
            state = 'Normal'

        return Message(str(datetime.now()), self.name, value, state, diff)