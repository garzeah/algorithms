class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}

        for word in strs:
            sort = "".join(sorted(word))

            if sort not in freq_map:
                freq_map[sort] = []

            freq_map[sort].append(word)

        return freq_map.values()

# Time Complexity: O(m * n * log(n)) where m is the length
# of how many input string we are given

# Space Complexity: O(n)