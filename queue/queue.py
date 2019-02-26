class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        # add the item the to storage
        self.storage.append(item)
        # increase the size of the array by 1
        self.size += 1

    def dequeue(self):
        # base case if the array is empty
        if self.size == 0:
            return None
        # decrement the size of the array by 1
        # pops the 0th index item and returns it
        else:
            self.size -= 1
            return self.storage.pop(0)

    def len(self):
        # returns the length of the array
        return self.size


print(Queue)
