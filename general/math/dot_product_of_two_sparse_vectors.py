class SparseVector:
    def __init__(self, nums: List[int]):
        # For every number that is not 0, we want to cache it
        self.nums = { i: num for i, num in enumerate(nums) if num }

    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0

        # Want to process the smaller array first because we only want
        # the dot product up until the end of the shortest array
        if len(self.nums) < len(vec.nums):
            for idx in self.nums.keys():
                if idx in vec.nums:
                    res += self.nums[idx] * vec.nums[idx]
        # Either vec.nums is shorter or they are both equal so we want to process
        # vec.nums.keys first if it's shorter or either if it's equal
        else:
            for idx in vec.nums.keys():
                if idx in self.nums:
                    res += self.nums[idx] * vec.nums[idx]

        return res

# Time Complexity: O(min(dict))
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/discuss/926985/Python-3-greater-99.16-faster