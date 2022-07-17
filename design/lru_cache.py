class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    # In order to implement an LRU cache efficiently we want...
    # - Fast lookup (hash map)
    # - Be able to easily remove a value and rearrange the
    # ordering (doubly linked list)
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Map key to nodes

        # left = LRU and right = recently used and we want nodes to be
        # connected in the event we're inserting a new node, we want
        # to put it in the middle of left and right
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Removing node from doubly linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next # Getting the back and front
        prev.next, nxt.prev = nxt, prev # Reconnecting without the node

    # Insert node before our right pointer (recently used)
    def insert(self, node):
        prev, curr = self.right.prev, self.right # Getting previous and current
        prev.next = curr.prev = node # Connecting prev and current to inserted node
        node.prev, node.next = prev, curr # Connecting inserted node to prev and current

    def get(self, key: int) -> int:
        if key in self.cache:
            # Removing and inserting puts it at the most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        # If we already have a node with the same key then we want to
        # remove from our list and overwriting it with the new key/value
        if key in self.cache:
            self.remove(self.cache[key])

        # Overwriting...
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If our cache exceeds the max capacity...
        if len(self.cache) > self.cap:
            # Remove the LRU from our cache and update left pointer
            lru = self.left.next # Because of our dummy nodes
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Time Complexity: O(1) for each method since we are not iterating
# through anything.

# Space Complexity: O(n) where n is the max capacity.