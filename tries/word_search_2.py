class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def addWord(self, word):
        curr = self

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.end_of_word = True

    # Removing word from trie if we find a match to improve TC
    def removeWord(self, word):
        curr = self

        # Want to get every node and its child
        nodeAndChildKey = [] # (TrieNode, str)
        for char in word:
            nodeAndChildKey.append((curr, char))
            curr = curr.children[char]

        # Removing process, want to remove from the bottom
        # because some words might share the same TrieNode
        for (parentNode, childKey) in reversed(nodeAndChildKey):
            curr = parentNode.children[childKey]

            # Remove the connections from parent to child if empty
            if len(curr.children) == 0:
                del parentNode.children[childKey]
            # Return since we are done deleting
            else:
                return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        # Want to perform DFS and for every letter in our matrix
        # we want to check if the current sequence of characters
        # is in our trie. This is a lot more optimal than
        # checking manually as shown in Word Search I
        def dfs(r, c, node, word):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children # More optimal cuz we can end earlier
            ):
                return

            visited.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.end_of_word:
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

# TC/SC: O(4^nm), brute force similar to word search I would have
# been O(len(words) * 4^nm) since the trie allows us to cancel early
# Solution: https://www.youtube.com/watch?v=asbcE9mZz_U