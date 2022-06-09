class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        # If 's' is a an odd number, we can't
        # have two subsets with same total
        if s % 2 != 0:
            return False

        # We are trying to find a subset of given numbers
        # that has a total sum of 's/2'.
        s = s // 2
        n = len(nums)
        dp = [[False for x in range(s+1)] for y in range(n)]

        # Populate the sum=0 column, as we can always have '0' sum
        # without including any element
        for i in range(0, n):
            dp[i][0] = True

        # With only one number, we can form a subset only when
        # the required sum is equal to its value
        for j in range(1, s+1):
            dp[0][j] = nums[0] == j

        # Process all subsets for all sums
        for i in range(1, n):
            for j in range(1, s+1):
                if dp[i - 1][j]: # If we can get the sum 'j' without the number at index 'i'
                    dp[i][j] = dp[i - 1][j]
                elif j >= nums[i]: # Else if we can find a subset to get the remaining sum
                    dp[i][j] = dp[i - 1][j - nums[i]]

        # The bottom-right corner will have our answer.
        return dp[n - 1][s]

# The above solution has time and space complexity of O(N*S), where ‘N’
# represents total numbers and ‘S’ is the total sum of all the numbers.