class Solution(object):
    def compress(self, chars):
        n = len(chars)

        # make it a bit faster
        if n < 2:
            return n

        # The start position of the contiguous group of characters we are currently reading
        anchor = 0

        # position to Write Next
        # we start with 0 then increase it whenever we write to the array
        write = 0

        # we go through each charcter till we find a pos where the next is not equal to it
        # then we check if it has appeared more than once using the anchor and write pointers
        # 1. iterate till we find a different char
        # 2. record the no. of times the current char was repeated
        for i, char in enumerate(chars):

            # check if we have reached the end or a different char
            # check if we are end or the next char != the current
            if (i + 1) >= n or chars[i] != chars[i + 1]:
                # Want to write the current character
                # - accounts for ["a", "2", "b", "2"]
                # - accounts for ["a", "b", "1", "2"]
                chars[write] = char
                write += 1

                # Only want to write when i is ahead of our anchor
                # - accounts for ["a"]
                if i > anchor:
                    # Check no. of times char has been repeated
                    repeated_times = i - anchor + 1

                    # Write the number, move it up incase of double digits
                    for num in str(repeated_times):
                        chars[write] = num
                        write += 1

                # Move the anchor to the next char in the iteration
                anchor = i + 1

        return write

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/string-compression/discuss/866955/Python-with-comments-(Explained)