class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # There are 3 cases we need to consider where...
        # 1) Someone can sit in the beginning
        # 2) Some can sit in the end
        # 3) Someone can sit between 2 people
        # Depending on which has the most zeroes, we can determine
        # which seat is the most optimal
        pre_zeros, suf_zeros, max_zeros, zeros = -1, -1, -1, 0
        for seat in seats:
            if seat == 0:
                zeros += 1
            # Reached the end of an empty seats
            else:
                # Recording the first set of zeros we find
                if pre_zeros == -1:
                    pre_zeros = zeros
                # Recording all zeros
                else:
                    max_zeros = max(max_zeros, zeros)

                zeros = 0 # Resetting our counter

        # Recording the last set of zeros in the end
        suf_zeros = zeros
        return max(pre_zeros, suf_zeros, (max_zeros + 1) // 2)

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/maximize-distance-to-closest-person/discuss/1693404/C%2B%2BJavaPython-One-Pass-O(N)-oror-Count-Zeros-oror-Image-Explained