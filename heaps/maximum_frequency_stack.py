# Refer to this solution: https://www.youtube.com/watch?v=Z6idIicFDOE

class FreqStack:
    def __init__(self):
        self.count = {}
        self.stacks = {}
        self.max_count = 0


    def push(self, val: int) -> None:
        val_count = 1 + self.count.get(val, 0)
        self.count[val] = val_count

        if val_count > self.max_count:
            self.max_count = val_count
            self.stacks[val_count] = []
        self.stacks[val_count].append(val)

    def pop(self) -> int:
        output = self.stacks[self.max_count].pop()
        self.count[output] -= 1

        if not self.stacks[self.max_count]:
            self.max_count -= 1

        return output


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()