class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map, max_heap, output = {}, [], []

        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        # Add all characters to the max heap
        for char, frequency in freq_map.items():
            heappush(max_heap, [-frequency, char])

        prev_char, prev_freq = None, 0
        while max_heap:
            frequency, char = heappop(max_heap)

            # Add the previous entry back in the heap if its frequency is greater than zero
            if prev_char and -prev_freq > 0:
                heappush(max_heap, [prev_freq, prev_char])

            # Append the current character to the result string and decrement its count
            output.append(char)
            prev_char = char
            prev_freq = frequency + 1  # Decrement the frequency

        # If we were successful in appending all the characters to the result string, return it
        return "".join(output) if len(output) == len(s) else ""

# Time Complexity: The time complexity of the above algorithm is O(N*logN)
# where ‘N’ is the number of characters in the input string.

# Space Complexity: The space complexity will be O(N), as in the worst case,
# we need to store all the ‘N’ characters in the HashMap.