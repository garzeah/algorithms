class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(reversed(digits))
        i = 0

        while True:
            if i < len(digits):
                if digits[i] == 9: # Set it to 0
                    digits[i] = 0
                else: # Add one to it normally
                    digits[i] += 1
                    break
            # When i reaches out of bounds,
            # we have to carry the 1 over
            else:
                digits.append(1)
                break

            i += 1

        return list(reversed(digits))

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=5iDkr6ebPuY