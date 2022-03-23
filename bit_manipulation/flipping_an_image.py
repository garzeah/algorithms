class Solution:
    def flipAndInvertImage(self, matrix: List[List[int]]) -> List[List[int]]:
        C = len(matrix)
        for row in matrix:
            for i in range((C+1)//2):
                row[i], row[C - i - 1] = row[C - i - 1] ^ 1, row[i] ^ 1

        return matrix

# Time Complexity: O(n)
# Space Complexity: O(1)