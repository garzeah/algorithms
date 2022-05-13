class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map, max_heap, output = Counter(s), [], []

        # Add all characters to the max heap
        for char, frequency in freq_map.items():
            heappush(max_heap, [-frequency, char])

        prev_char, prev_freq = None, None
        while max_heap:
            frequency, char = heappop(max_heap)

            # Since we only want a freq. that is > 0, we will only
            # be able to append adj. characters since we can't
            # add in the same consecutive character unless
            # a different character comes before it
            if prev_freq > 0:
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