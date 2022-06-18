class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            # Create a TrieNode for the letter if it doesn't exist
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char] # Moving to next letter

        curr.end_of_word = True


    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False

            curr = curr.children[char]

        return curr.end_of_word


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False

            curr = curr.children[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Time Complexity:
# - insert(word): O(n) where n is the length of the word
# - search(word): O(n) where n is the length of the word
# - startsWith(prefix): O(n) where n is the length of the word

# Space Complexity: O(n * m) where n is the number of words
# and m is the max length. This would cover all of the
# possible words contained in our trie.

# Solution: https://www.youtube.com/watch?v=oobqoCJlHA0