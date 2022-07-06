class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map, heap, res = Counter(s), [], []

        for char, freq in freq_map.items():
            heappush(heap, [-freq, char])

        prev_char, prev_freq = None, None
        while heap:
            freq, char = heappop(heap)

            # If the prev_char's frequency is not 0 then we are allowed
            # to use the character again in reorganizing the string as
            # long as there is a value in our heap
            if prev_freq:
                heappush(heap, [prev_freq, prev_char])

            res.append(char)
            prev_char = char
            prev_freq = freq + 1

        return "".join(res) if len(res) == len(s) else ""

# Time Complexity: The time complexity of the above algorithm is O(N*logN)
# where ‘N’ is the number of characters in the input string.

# Space Complexity: The space complexity will be O(N), as in the worst case,
# we need to store all the ‘N’ characters in the HashMap.

# Solution: https://www.youtube.com/watch?v=2g_b1aYTHeg