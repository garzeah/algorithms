class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1 # Adding 1 to the end

            # After adding 1, if it equals 10 then set to 0 bc of carry over
            if digits[i] == 10:
                digits[i] = 0

            # Otherwise, we don't have to carry and can return the array
            else:
                return digits

        return [1] + digits # Accounting for carry

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/plus-one/discuss/24091/Easy-Python-solution-O(n)/606428