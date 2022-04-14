class Solution:
    def get_next_valid_char_index(str, index):
        backspace_count = 0
        while (index >= 0):
            if str[index] == '#':  # Found a backspace character
                backspace_count += 1
            elif backspace_count > 0:  # A non-backspace character
                backspace_count -= 1
            else:
                break

            index -= 1  # Skip a backspace or a valid character

        return index

    def backspaceCompare(self, str1: str, str2: str) -> bool:
        # Use two pointer approach to compare the strings
        index1 = len(str1) - 1
        index2 = len(str2) - 1

        # Have to use or
        while (index1 >= 0 or index2 >= 0):
            i1 = Solution.get_next_valid_char_index(str1, index1)
            i2 = Solution.get_next_valid_char_index(str2, index2)
            if i1 < 0 and i2 < 0:  # Reached the end of both the strings
                return True
            if i1 < 0 or i2 < 0:  # Reached the end of one of the strings
                return False
            if str1[i1] != str2[i2]:  # Check if the characters are equal
                return False

            index1 = i1 - 1
            index2 = i2 - 1

        return True

# Time Complexity: The time complexity of the above algorithm will be O(M+N)
# where ‘M’ and ‘N’ are the lengths of the two input strings respectively.

# Space Complexity: O(1)