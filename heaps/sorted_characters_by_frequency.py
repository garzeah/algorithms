class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map, max_heap, output = {}, [], []

        # Find the frequency of each character
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        # Add all characters to the max heap
        for char, frequency in freq_map.items():
            heappush(max_heap, (-frequency, char))

        # Build a string, appending the most occurring characters first
        while max_heap:
            frequency, char = heappop(max_heap)
            for _ in range(-frequency):
                output.append(char)

        return ''.join(output)

# Time Complexity: The time complexity of the above algorithm is O(D*logD)
# where ‘D’ is the number of distinct characters in the input string. This
# means, in the worst case, when all characters are unique the time
# complexity of the algorithm will be O(N*logN) where ‘N’ is the
# total number of characters in the string.

# Space Complexity: The space complexity will be O(N), as in the worst
# case, we need to store all the ‘N’ characters in the HashMap.