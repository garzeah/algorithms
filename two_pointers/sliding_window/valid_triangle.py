class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Keep things in descending order because we want
        # to compare a + b with the highest value
        nums = sorted(nums)
        res = 0

        #  0 1 2 3
        # [2,2,3,4]
        #  a   b c  = 2
        #  a b   c  = 0
        #  a b c    = 1

        # We can find a valid triangle using the property a + b > c
        for i in range(len(nums) - 1, -1, -1):
            a, b, c = 0, i - 1, i

            while a < b:
                # Since a + b > c, we can find the total amount of valid triangles by
                # subtracting getting the distance from b to a. Since b will have
                # bigger values, we can look at the smaller values and see if we
                # can form a valid triangle
                if nums[a] + nums[b] > nums[c]:
                    res += b - a
                    b -= 1
                # We want to find a bigger value that can help us form a valid triangle
                else:
                    a += 1

        return res

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/valid-triangle-number/discuss/487683/Python-O(-n2-)-sol.-based-on-sliding-window-and-sorting.-85%2B-With-explanation