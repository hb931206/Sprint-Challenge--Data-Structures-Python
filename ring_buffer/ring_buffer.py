class RingBuffer:
    def __init__(self, capacity, ):
        self.capacity = capacity
        self._data = []
        self.index = 0

    def append(self, value):
        if len(self._data) == self.capacity:
            self._data[self.index] = value
        else:
            self._data.append(value)
        self.index = (self.index+1) % self.capacity

    def get(self):
        return self._data


# If I'm not at the constraint add to the list
# If I'm at the constaint, remove the oldest one then add it
# Look at doubley linked list.
# first in first out = Queue
