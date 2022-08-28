class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        # Taking a greedy approach and want to get the
        # most units per boxes in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res = 0

        for boxes, units in boxTypes:
            # When our truck is almost full and we still have remaining boxes,
            # we only want to put truckSize amount so we don't excee the capacity
            numOfBoxes = min(boxes, truckSize)
            res += numOfBoxes * units # Appending the units
            truckSize -= numOfBoxes # Decreasing truck size

            if truckSize == 0: return res

        return res

# Time Complexity: O(nlogn)
# Space Complexuty: O(1)
# Solution: https://leetcode.com/problems/maximum-units-on-a-truck/discuss/1271374/JS-Python-Java-C%2B%2B-or-Simple-Sort-Solution-w-Explanation