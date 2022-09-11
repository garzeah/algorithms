class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to_rank = {}

        rank = 1
        for num in sorted(arr):
            if num not in num_to_rank:
                num_to_rank[num] = rank
                rank += 1

        res = []
        for num in arr:
            res.append(num_to_rank[num])

        return res

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

