class MinStack:

    def __init__(self):
        self.stack = []

    # We can consider each "node" in the stack having
    # a minimum value if we have a MinStack
    def push(self, val: int) -> None:
        min_num = float('inf')
        if self.stack:
            min_num = min(self.stack[-1][1], val)
        else:
            min_num = val
        self.stack.append((val, min_num))


    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Time Complexity: O(1)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=qkLl7nAwDPo