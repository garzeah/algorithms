# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def findShips(topRight, bottomLeft):
            # Base case of reaching singularity (1 single point)
            if (
                topRight.x == bottomLeft.x and
                topRight.y == bottomLeft.y
            ):
                return int(sea.hasShips(topRight, bottomLeft))

            # Base case for when we are out of bounds or when there aren't any ships
            if (
                topRight.x < bottomLeft.x or
                topRight.y < bottomLeft.y or
                sea.hasShips(topRight, bottomLeft) is False
            ):
                return 0

            # Finding the midpoint of bottomLeft and topRight
            midX = (bottomLeft.x + topRight.x) // 2
            midY = (bottomLeft.y + topRight.y) // 2
            mid = Point(midX, midY)

            # Since we are limited to having a 1000 then that means the maximum
            # area we have to search for each ship is 1 million. However, we
            # have to consider that there are at most 10 ships and we cannot
            # make more than 400 calls. A good way to perform our search is
            # in quadrants of 4 because if we do log base 4 of 1 million
            # we end up with a value that approximately equals 10.

            # Moving topLeftQ and topRightQ to prevent overlap with the bottom
            # quadrants and moving botRightQ to prevent overlap with the botLeftQ
            topLeftQ = findShips(Point(mid.x, topRight.y), Point(bottomLeft.x, mid.y + 1))
            topRightQ = findShips(topRight, Point(mid.x + 1, mid.y + 1))
            botLeftQ = findShips(mid, bottomLeft)
            botRightQ = findShips(Point(topRight.x, mid.y), Point(mid.x + 1, bottomLeft.y))

            return topLeftQ + topRightQ + botLeftQ + botRightQ

        return findShips(topRight, bottomLeft)

# Time and Space Complexity: log(m, n)^2 where m and n is the number
# of rows and cols of our rectangle. And it is squared
# since we are basically doing log(n) twice
# Solution: https://www.youtube.com/watch?v=fZXyxGTqlgQ