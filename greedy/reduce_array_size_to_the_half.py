class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total = 0
        freq = sorted(list(Counter(arr).values()), reverse=True) # sort by highest freq

        # Getting the frequency and starting with the highest frequency first
        for (i, frequency) in enumerate(freq):
            total += frequency

            # We have reduced the array size to half, so we want
            # to return how many set of dupes we had to remove
            if total >= len(arr) // 2:
                return i + 1

        return 0

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/2442400/Short-oror-C%2B%2B-oror-Java-oror-PYTHON-oror-Explained-Solution-oror-Beginner-Friendly-oror-BY-MR-CODER