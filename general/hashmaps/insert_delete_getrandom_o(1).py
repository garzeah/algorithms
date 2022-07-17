class RandomizedSet:

    def __init__(self):
        self.map = {} # val to index pos. in list
        self.list = [] # list of indexes corresponding to map


    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val] = len(self.list)
        self.list.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val in self.map:
            removed_idx = self.map[val] # Get the index of the value being removed
            last_val = self.list[-1] # Get the last index for replacement
            self.list[removed_idx] = last_val # Put the last index in the removed position
            self.list.pop() # Remove the last index now that we have copied it
            self.map[last_val] = removed_idx # Update mapping for last val
            del self.map[val] # Removing value from our map
            return True

        return False


    def getRandom(self) -> int:
        return random.choice(self.list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Time Complexity: O(1)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=j4KwhBziOpg