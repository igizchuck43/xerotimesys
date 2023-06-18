class Queue:
  def __init__(self):
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
  queue.enqueue(1)
  queue.enqueue(2)
  queue.enqueue(3)
  print(queue.peek())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.is_empty())
