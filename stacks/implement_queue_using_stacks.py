class MyQueue:

    def __init__(self):
        self.dummy, self.queue = [], []

    def push(self, x: int) -> None:
        # When adding a new value, we want to
        # pop every value from our queue into
        # dummy then add the new value in
        while self.queue:
            self.dummy.append(self.queue.pop())

        # When pushing a value to an empty queue, we want to
        # push every value into dummy then pop it and add it
        # into our queue so it's in FIFO order.
        self.dummy.append(x)
        while self.dummy:
            self.queue.append(self.dummy.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Time Complexity:
#   - push(self, x: int): O(n)
#   - pop(self): O(1)
#   - peek(self): O(1)
#   - empty(self): O(1)

# Space Complexity: O(n)