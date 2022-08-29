class RandomizedCollection:
    def __init__(self):
        self.nums = [] # Numbers mapped to their index
        self.d = defaultdict(set) # Val to set of indexes


    def insert(self, val: int) -> bool:
        # Value already exists in our hashset, return false
        if val in self.d and len(self.d[val]) > 0:
            res = False
        else: # otherwise, return true
            res = True

        self.nums.append(val)
        self.d[val].add(len(self.nums) - 1) # Store index positions

        return res


    def remove(self, val: int) -> bool:
        # If we already have an existing index in our set then
        # we want to remove it or remove one of the dupes
        if val in self.d and len(self.d[val]) > 0:
            idx = self.d[val].pop() # removes a random index from our set
            last_idx = len(self.nums) - 1 # get the last position
            last_val = self.nums[last_idx] # get the last val

            # Update our hashset to have the index of val since we will
            # swap and remove its current index
            self.d[last_val].add(idx)
            self.d[last_val].remove(last_idx)

            # Swap the positions of the current val and last val and remove the last val
            self.nums[idx], self.nums[last_idx] = self.nums[last_idx], self.nums[idx]
            self.nums.pop() # Remove the value designated value

            return True

        return False


    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Solution: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/discuss/1586322/Python-99.61-with-comments-use-dict-hash-and-a-list