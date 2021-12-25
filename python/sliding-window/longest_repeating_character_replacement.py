class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, max_repeat, max_length = 0, 0, 0;
        freq_map = {};

        for end in range(len(s)):
            right_elem = s[end]

            if right_elem not in freq_map:
                freq_map[right_elem] = 0

            freq_map[right_elem] += 1
            max_repeat = max(max_repeat, freq_map[right_elem])

            # Current window size is from 'start' to 'end', overall we have a letter which is
            # repeating 'max_repeat' times, this means we can have a window which has one letter
            # repeating 'max_repeat' times and the remaining letters we should replace.if the
            # remaining letters are more than 'k', it is the time to shrink the window as we
            # are not allowed to replace more than 'k' letters
            while ((end - start + 1 - max_repeat) > k):
                left_elem = s[start]
                freq_map[left_elem] -= 1

                if freq_map[left_elem] == 0:
                    del freq_map[left_elem]

                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length