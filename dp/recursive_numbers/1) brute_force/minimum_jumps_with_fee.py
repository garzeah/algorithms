def min_fee(fee, n):
    if n <= 0:
        return 0

    one_step = fee[n - 1] + min_fee(fee, n - 1)
    two_step = fee[n - 2] + min_fee(fee, n - 2)
    three_step = fee[n - 3] + min_fee(fee, n - 3)

    return min(one_step, two_step, three_step)