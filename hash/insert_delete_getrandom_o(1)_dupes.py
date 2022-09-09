class RandomizedCollection:
    def __init__(self):
        self.arr = [] # Numbers mapped to their index
        self.map = defaultdict(set) # Val to set of indexes


    def insert(self, val: int) -> bool:
        # Value already exists in our hashset, return false
        if val in self.map and len(self.map[val]) > 0:
            res = False
        else: # otherwise, return true
            res = True

        self.arr.append(val)
        self.map[val].add(len(self.arr) - 1) # Store index positions

        return res


    def remove(self, val: int) -> bool:
        # If we already have an existing index in our set then
        # we want to remove it or remove one of the dupes
        if val in self.map and len(self.map[val]) > 0:
            remove_idx = self.map[val].pop() # removes a random index from our set
            last_idx = len(self.arr) - 1 # get the last position
            last_val = self.arr[last_idx] # get the last val

            # Update our hashset to have the index of val since we will
            # swap and remove its current index
            self.map[last_val].add(remove_idx)
            self.map[last_val].remove(last_idx)

            # Swap the positions of the current val and last val and remove the last val
            self.arr[remove_idx], self.arr[last_idx] = self.arr[last_idx], self.arr[remove_idx]
            self.arr.pop() # Remove the value designated value

            return True

        return False


    def getRandom(self) -> int:
        return choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Solution: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/discuss/1586322/Python-99.61-with-comments-use-dict-hash-and-a-list