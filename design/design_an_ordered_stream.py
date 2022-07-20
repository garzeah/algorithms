class OrderedStream:

    def __init__(self, n: int):
        self.list = [None] * n
        self.i = 0


    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey - 1] = value
        res = []

        # While we're in bounds and we have a valid value...
        while self.i < len(self.list) and self.list[self.i]:
            if self.list[self.i] is None:
                return []

            res.append(self.list[self.i])
            self.i += 1

        return res




# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

# Time Complexity: O(n) where n is the amount of values we have in our list
# Space Complexity: O(n) where n is the amount of values we have in our list