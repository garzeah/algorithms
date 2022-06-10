class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        # If 'target' is a an odd number, we can't
        # have two subsets with same total
        if target % 2 == 1:
            return False

        # We are trying to find a subset of given numbers
        # that has a total sum of 'target/2'.
        target = target // 2
        n = len(nums)
        # x represents target and y represents num/sums
        dp = [[False for x in range(target + 1)] for y in range(n)]

        # Populate the sum = 0 column, as we can always have '0' sum
        # without including any element
        for i in range(0, n):
            dp[i][0] = True

        # Process the first row since with only one number, we can form
        # a subset only when the required sum is equal to its value
        for target in range(1, target + 1):
            dp[0][target] = nums[0] == target

        # Process all subsets for all sums
        for idx in range(1, n):
            for target in range(1, target + 1):
                # Check the previous to see if we can get the sum
                # 'target' without the number at index 'idx'
                if dp[idx - 1][target]:
                    dp[idx][target] = dp[idx - 1][target]
                # Else if we can find a subset to get the remaining sum
                elif target >= nums[idx]:
                    dp[idx][target] = dp[idx - 1][target - nums[idx]]

        # The bottom-right corner will have our answer.
        return dp[n - 1][target]

# The above solution has time and space complexity of O(N*S), where ‘N’
# represents total numbers and ‘S’ is the total sum of all the numbers.