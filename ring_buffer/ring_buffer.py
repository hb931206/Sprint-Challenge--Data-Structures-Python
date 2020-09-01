

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[0] = item

    def get(self):
        return self.data


# If I'm not at the constraint add to the list
# If I'm at the constaint, remove the oldest one then add it
# Look at doubley linked list.
# first in first out = Queue
