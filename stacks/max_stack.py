class MaxStack:
    def __init__(self):
        self.stack = []

    # Time Complexity: O(1)
    def push(self, x):
        # If the new value is greater than our current
        # highest then we need to record a new index
        if self.stack and x >= self.stack[self.stack[-1][1]][0]:
            i = len(self.stack)
        # Otherwise, we want to use the prev_max idx
        # since there's no new max yet
        else:
            i = self.stack[-1][1] if self.stack else 0

        self.stack.append((x, i))

    # Time Complexity: O(1)
    def pop(self):
        return self.stack.pop()[0]

    # Time Complexity: O(1)
    def top(self):
        return self.stack[-1][0]

    # Time Complexity: O(1)
    def peekMax(self):
        return self.stack[self.stack[-1][1]][0]

    # Time Complexity: O(n)
    def popMax(self):
        max_idx = self.stack[-1][1]  # index where the max exists
        res = self.stack[max_idx][0]  # max value to return
        prev_max = self.stack[self.stack[max_idx - 1][1]][0] if max_idx > 0 else float('-inf')

        # Scan the stack starting at 'index' to recompute the max values and shift all
        # values to the left by one:
        for i in range(max_idx, len(self.stack) - 1):
            # We can keep the value and just shift it left
            # since we don't have to record a new max
            if prev_max <= self.stack[i + 1][0]:
                prev_max = self.stack[i + 1][0] # Update prev_max
                self.stack[i] = (prev_max, i)
            # Since our prev_max is greater than the value ahead,
            # we need to update the values ahead with our new max
            else:
                self.stack[i] = (self.stack[i + 1][0], self.stack[i - 1][1])

        self.stack.pop()
        return res

# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/max-stack/discuss/391403/Python-O(1)-push-pop-top-and-peekMax-O(N)-popMax


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()