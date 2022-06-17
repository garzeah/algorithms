class TimeMap:

    def __init__(self):
        self.store = {} # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res = ""

        # Using get because if it doesn't return a value
        # we can default it by adding a parameter
        values = self.store.get(key, [])

        # Binary search
        l, r = 0, len(values) - 1
        while l <= r: # Equal bc we want to get the last value
            mid = (l + r) // 2

            # Less than and equal to because we want
            # the closest value to our target
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Time Complexity:
#   - set(key, value, timestamp): O(1)
#   - get(key, timestamp): O(log(n))

# Space Complexity:
#   - TimeMap: O(n)
#   - set(key, value, timestamp): O(1)
#   - get(key, timestamp): O(n)

# Solution: https://www.youtube.com/watch?v=fu2cD_6E8Hw