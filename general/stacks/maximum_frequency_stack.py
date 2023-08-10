class FreqStack:

    def __init__(self):
        self.count = {} # Value to frequency map
        # Frequency to array of nums w/ that frequency map
        self.stacks = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Recording the frequency
        frequency = self.count.get(val, 0) + 1
        self.count[val] = frequency

        # Want to record the new max frequency and add it
        # to our stack map that holds the frequency to
        # array of nums w/ that frequency
        if frequency > self.max_freq:
            self.max_freq = frequency
            self.stacks[frequency] = []

        self.stacks[frequency].append(val)

    def pop(self) -> int:
        # Popping the number with the highest frequency
        num = self.stacks[self.max_freq].pop()
        self.count[num] -= 1

        # If stacks has no more numbers left in that
        # frequency, then decrement the max count
        if len(self.stacks[self.max_freq]) == 0:
            self.max_freq -= 1

        return num

# Time Complexity: O(1)
# Space Complexity: O(n) for the sizes of our stacks map
# Solution: https://www.youtube.com/watch?v=Z6idIicFDOE