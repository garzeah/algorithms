class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            # If character not in trie, create new node
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()

            # Check the next node (letter)
            curr_node = curr_node.children[char]

        # For the last node, update the end of word flag
        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            # If character not in trie, it doesn't exist
            if char not in curr_node.children:
                return False

            # Check the next node (letter)
            curr_node = curr_node.children[char]

        return curr_node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for char in prefix:
            # If character not in trie, it doesn't start with
            if char not in curr_node.children:
                return False

            # Check the next node (letter)
            curr_node = curr_node.children[char]

        return True

# Time Complexity:
# insert(word) is O(n * m) where n is the number of words and m is the max length
# search(word) is O(m) where m is the max length
# startsWith(prefix) is O(m) where m is the max length

# Space Complexity: O(n * m) where n is the number of words and m is the max length.

# Solution: https://www.youtube.com/watch?v=oobqoCJlHA0