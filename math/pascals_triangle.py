class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []

        if numRows == 1: return [[1]]

        tri = [[1]]

        # For each row, we want to use the previous
        # row in the triangle to build up our rows
        for i in range(1, numRows):
            row = [1] # Left side of row

            # Building middle values of our row
            for j in range(1, i):
                row.append(tri[i - 1][j - 1] + tri[i - 1][j])

            row.append(1) # Right side of row
            tri.append(row)

        return tri

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/pascals-triangle/discuss/439724/Easy-to-understand-Python3-code-using-append