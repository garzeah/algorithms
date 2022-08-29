# A good way to approach this problem is to consider the
# tradeoffs. Are we trying to prioritize time, space or
# trying to find a balance between the both of them.

# Time Complexity: O(n + m)
# Space Complexity: O(m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)

        res = []
        for num in nums2:
            if num in count and count[num] > 0:
                res.append(num)
                count[num] = 0

        return res

# Time Complexity: O(n * m)
# Space Complexity: O(max(n, m))
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    res.add(nums1[i])

        return res