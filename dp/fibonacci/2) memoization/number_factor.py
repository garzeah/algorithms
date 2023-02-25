# Available numbers are 1, 3, and 4
def count_ways(n):
    memo = [ -1 for x in range(n + 1) ]
    return helper(n, memo)

def helper(n, memo):
    # Setting up our base cases
    # We can not get a negative target number at any point,
    # so we return 0 for negative values
    if n < 0:
        return 0

    # There is only 1 way to reach a target number of 0,
    # by not using any available numbers
    if n == 0:
        return 1

    if memo[n] != -1:
        return memo[n]

    # Recursively calculate the number of ways using the
    # recurrence relation
    memo[n] = helper(n - 1, memo) + helper(n - 3, memo) + helper(n - 4, memo)
    return memo[n]