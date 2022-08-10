class SparseVector:
	def __init__(self, nums: List[int]):
		self.seen = {} # index to val

        # Want to record every non-zero number in our hashmap
		for (idx, num) in enumerate(nums):
			if num != 0:
				self.seen[idx] = num

	# Return the dotProduct of two sparse vectors
	def dotProduct(self, vec: 'SparseVector') -> int:
		res = 0

        # So for each non-zero number in our vector's hashmap
        # we want to check if that exists in ours, if it does
        # append the results. This way save time by avoiding
        # calculating values with 0s
		for (idx, num) in vec.seen.items():
			if idx in self.seen:
				res += num * self.seen[idx]

		return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/discuss/825936/Python-dictionary