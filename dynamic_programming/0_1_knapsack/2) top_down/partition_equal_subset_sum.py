class Solution:
    def can_partition(self, num):
        s = sum(num)

        # if 's' is a an odd number, we can't have two subsets with equal sum
        if s % 2 != 0:
            return False

        # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
        dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(num))]
        return True if self.helper(dp, num, int(s / 2), 0) == 1 else False

    def helper(self, dp, num, sum, currentIndex):
        # base check
        if sum == 0:
            return 1

        n = len(num)
        if n == 0 or currentIndex >= n:
            return 0

        # if we have not already processed a similar problem
        if dp[currentIndex][sum] == -1:
            # recursive call after choosing the number at the currentIndex
            # if the number at currentIndex exceeds the sum, we shouldn't process this
            if num[currentIndex] <= sum:
                if self.helper(dp, num, sum - num[currentIndex], currentIndex + 1) == 1:
                    dp[currentIndex][sum] = 1
                    return 1

            # recursive call after excluding the number at the currentIndex
            dp[currentIndex][sum] = self.helper(dp, num, sum, currentIndex + 1)

        return dp[currentIndex][sum]