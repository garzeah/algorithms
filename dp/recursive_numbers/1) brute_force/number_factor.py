# Available numbers are 1, 3, and 4
def count_ways(n):

    # Setting up our base cases
    # We can not get a negative target number at any point,
    # so we return 0 for negative values
    if n < 0:
        return 0

    # There is only 1 way to reach a target number of 0,
    # by not using any available numbers
    if n == 0:
        return 1

    # Recursively calculate the number of ways using the
    # recurrence relation
    return count_ways(n - 1) + count_ways(n - 3) + count_ways(n - 4)