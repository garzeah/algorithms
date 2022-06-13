class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_num = (0, 0)

        for key in count:

            if count[key] > max_num[1]:
                max_num = (key, count[key])

        return max_num[0]

# Time Complexity: O(n)
# Space Complexity: O(n)