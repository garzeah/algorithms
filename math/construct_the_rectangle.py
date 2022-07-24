class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        L = W = int(sqrt(area))

        while L*W != area:
            if L*W < area:
                L += 1
            else:
                W -= 1

        return [L, W]

# Time Complexity: O(n)
# Space Complexity: O(1)