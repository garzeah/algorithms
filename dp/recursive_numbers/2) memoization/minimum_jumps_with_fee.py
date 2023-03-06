def min_fee(fee, n):
    memo = {}
    return helper(fee, n, memo)

def helper(fee, n, memo):
    if n <= 0:
        return 0

    if n in memo:
        return memo[n]

    one_step = fee[n - 1] + helper(fee, n - 1, memo)
    two_step = fee[n - 2] + helper(fee, n - 2, memo)
    three_step = fee[n - 3] + helper(fee, n - 3, memo)
    memo[n] = min(one_step, two_step, three_step)
    return memo[n]