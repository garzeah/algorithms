class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    # Space Complexity: O(n * m) where n is the number of words
    # we insert into our tries and m is the max length
    def __init__(self):
        self.root = TrieNode()

    # Time Complexity: O(n) where n is the amout of characters
    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        curr.end_of_word = True


    # Time Complexity: O(26^n) since we may have 26 possible choices
    # per trie worst case scenarion
    def search(self, word: str) -> bool:
        def dfs(start, root):
            curr = root

            for i in range(start, len(word)):
                char = word[i]
                # For each child, we have to perform
                # DFS/Backtracking until we get a match
                if char == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True

                    return False

                else:
                    if char not in curr.children:
                        return False

                    curr = curr.children[char]
            return curr.end_of_word

        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Solution: https://www.youtube.com/watch?v=BTf05gs_8iU