class FreqStack:

    def __init__(self):
        # stacks will be a map of frequency and contain an
        # array of numbers that have that frequency
        self.freq_map, self.stacks = {}, {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Recording the frequency
        frequency = self.freq_map.get(val, 0) + 1
        self.freq_map[val] = frequency

        # Want to record the new max frequency and add a new
        # key value pair to store those values that have that frequency
        if frequency > self.max_freq:
            self.max_freq = frequency
            self.stacks[frequency] = []

        self.stacks[frequency].append(val)

    def pop(self) -> int:
        # Popping the number with the highest frequency
        num = self.stacks[self.max_freq].pop()
        self.freq_map[num] -= 1

        # If stacks has no more numbers left in that
        # frequency, then decrement the max count
        if len(self.stacks[self.max_freq]) == 0:
            self.max_freq -= 1

        return num

# Time Complexity: O(1) for both push and pop
# Space Complexity: O(n) for the sizes of our stacks map
# Solution: https://www.youtube.com/watch?v=Z6idIicFDOE