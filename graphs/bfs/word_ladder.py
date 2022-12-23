class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # No path exists from beginning to end
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        wordList.append(beginWord)

        # Find every possible pattern for this
        # word and build out our adjaceny list
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)

        queue, visited = deque([beginWord]), set()
        res = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                visited.add(word)

                if word == endWord:
                    return res

                # Checking the patterns for this word
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]

                    for nei in adj[pattern]: # Checking neighbors
                        if nei not in visited:
                            queue.append(nei)

            res += 1 # Only add after we go through each layer

        return 0

# TC: Generating the adj. list is O(n * m^2) and performing BFS is O(n^2 * m) where
# n is len(w) <= 10 and m is len(list) <= 5000
# SC: O(V) + O(E) where V is every possible pattern and E is every edge
# Solution: https://www.youtube.com/watch?v=h9iTnkgv05E