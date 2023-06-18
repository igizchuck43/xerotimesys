class Queue:
    def __intit__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.peek())