# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    # TC: O(1)
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # Storing a stack of arrays where we have our nestedList
        # and a pointer to the start of our nestedList
        self.stack = [[nestedList, 0]]

    # TC: O(1)
    def next(self):
        """
        :rtype: int
        """
        # Destructuring the most recent value in our stack
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1 # Moving the pointer up

        return nestedList[i].getInteger()

    # TC: O(n)
    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack

        while s:
            nestedList, i = s[-1]

            # If we reach the end of our nestedList, remove it
            if i == len(nestedList):
                s.pop()

            # Otherwise, iterate through the list and checked if
            # there are still some integers in the nested list
            else:
                x = nestedList[i]

                # Means there are still some integers in the nested list
                if x.isInteger():
                    return True

                # Otherwise, we have a list so we move up the pointer
                # and append the list to our stack and starting pointer
                s[-1][1] += 1
                s.append([x.getList(), 0])

        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80146/Real-iterator-in-Python-Java-C%2B%2B