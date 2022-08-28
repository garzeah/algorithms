class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(mat), len(mat[0])

        if ROWS * COLS != r * c:
            return mat

        res = [[]]
        for row in range(ROWS):
            for col in range(COLS):
                num = mat[row][col]

                # Add values to our nested list as long as it is less than c
                if len(res[-1]) < c:
                    res[-1].append(num)
                # Create a new column to append to our list
                else:
                    res.append([num])
        return res

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Solution: https://leetcode.com/problems/reshape-the-matrix/discuss/102516/Easy-to-understand-python-solution