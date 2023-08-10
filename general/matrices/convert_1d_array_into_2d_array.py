class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        output = []
        if len(original) != m * n:
            return output

        # For every n steps in our array...
        for i in range(0, len(original), n):
            # We want to append an array of n elements
            output.append(original[i : i + n])

        return output

# Time Complexity: O(n)
# Space Complexity: O(n)