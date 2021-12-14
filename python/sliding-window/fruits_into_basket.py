from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_length = float('-inf')
        start = 0
        freq = {}

        # try to extend the range [window_start, window_end]
        for end in range(len(fruits)):
            right_elem = fruits[end]

            if right_elem not in freq:
                freq[right_elem] = 0

            freq[right_elem] += 1

            # shrink the sliding window, until we are left
            # with '2' fruits in the fruit frequency dictionary
            while len(freq) > 2:
                # since > 2, start shrinking the window
                left_elem = fruits[start]
                freq[left_elem] -= 1

                if freq[left_elem] == 0:
                    del freq[left_elem]

                # shrink the window
                start += 1

            # calculate the max_length once we know that we are not > 2
            max_length = max(max_length, end - start + 1)

        return max_length
