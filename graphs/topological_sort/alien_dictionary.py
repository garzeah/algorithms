class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""

        # a. Initialize the graph
        in_degree, adj = {}, {}  # Count of incoming edges and adj. list
        for word in words:
            for char in word:
                adj[char] = []
                in_degree[char] = 0

        # b. Build the graph
        for i in range(len(words) - 1):
            # Find ordering of characters from adjacent words
            w1, w2 = words[i], words[i + 1]
            min_length = min(len(w1), len(w2))

            for char in range(min_length):
                parent, child = w1[char], w2[char]

                # Since it is lexicographically sorted in the alien's dictionary, we
                # want to find out where the characters differ so we can use that
                # information to see which letter comes first. Then we can use
                # the toplogical sort algorithm to create a word in lexicographic order
                if parent != child:
                    # Put the child into it's parent's list
                    adj[parent].append(child)
                    in_degree[child] += 1  # Increment child's in_degree
                    break  # Break since we only want to find the first occurence of where they're different

                # An edge case we need to consider is that if the prefix of
                # the words are the exact same but the 1st word is larger
                # than the 2nd word then we have an invalid ordering
                if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                    return ""

        # c. Find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the sorted_order and subtract one
        # from all of its children's in-degrees if a child's in-degree
        # becomes zero, add it to the sources queue.
        sorted_order = []
        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)

            for child in adj[vertex]:  # Get the node's children to decrement their in-degrees
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        # If sorted_order doesn't contain all characters, there
        # is a cyclic dependency between characters, therefore, we
        # will not be able to find the correct ordering of the characters
        if len(sorted_order) != len(in_degree):
            return ""

        return "".join(sorted_order)

# Time Complexity: In step ‘d’, each task can become a source only once and
# each edge (a rule) will be accessed and removed once. Therefore, the time
# complexity of the above algorithm will be O(V+E), where ‘V’ is the total
# number of different characters and ‘E’ is the total number of the rules
# in the alien language. Since, at most, each pair of words can give us
# one rule, therefore, we can conclude that the upper bound for the
# rules is O(N) where ‘N’ is the number of words in the input. So,
# we can say that the time complexity of our algorithm is O(V+N).

# Space Complexity: The space complexity will be O(V+N), since we
# are storing all of the rules for each character in an adjacency list.

# Solution: https://www.educative.io/courses/grokking-the-coding-interview/R8AJWOMxw2q