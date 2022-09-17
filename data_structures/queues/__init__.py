class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.item = [None] * capacity
        self.head = None
        self.tail = None
        self.size = 0
    def is_full(self):
        if self.head is None:
            return False
        if (self.tail + 1) % self.capacity == self.head:
            return True
    def enqueue(self, value):
        if self.is_full():
            raise Exception("队列已满")
        if self.size == 0:
            self.head = 0
            self.tail = 0
            self.item[self.tail] = value
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.item[self.tail] = value
        self.size += 1
    def dequeue(self):
        if self.size == 0:
            raise Exception("队列为空")
        # 队列只有一个元素
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = (self.head + 1) % self.capacity
        self.size -= 1

