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
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return int(sea.hasShips(topRight, bottomLeft))

            # Base case for when we are out of bounds or when there aren't any ships
            if (
                topRight.x < bottomLeft.x or topRight.y < bottomLeft.y or
                sea.hasShips(topRight, bottomLeft) is False
            ):
                return 0

            # Finding the midpoint of bottomLeft and topRight
            midX = (bottomLeft.x + topRight.x) // 2
            midY = (bottomLeft.y + topRight.y) // 2
            mid = Point(midX, midY)

            # We are going to perform our search in 4 separate quadrants because let's say
            # we have a 10*10 rectangle, that means there are 100 points to look at total
            # and we can keep dividing the quadrants to 4ths, 16ths, 64ths, etc. and if
            # we do that we can consider that log base 4 of any number will be small
            # considering that there are at most 10 ships and it'd be easier to
            # search in that manner

            # Adding 1 to prevent overlapping boundaries
            topLeftQ = findShips(Point(mid.x, topRight.y), Point(bottomLeft.x, mid.y + 1))
            topRightQ = findShips(topRight, Point(mid.x + 1, mid.y + 1))
            botRightQ = findShips(Point(topRight.x, mid.y), Point(mid.x + 1, bottomLeft.y))
            botLeftQ = findShips(mid, bottomLeft)

            return topLeftQ + topRightQ + botRightQ + botLeftQ

        return findShips(topRight, bottomLeft)

# Time and Space Complexity: log(m, n)^2 where m and n is the number
# of rows and cols of our rectangle. And it is squared
# since we are basically doing log(n) twice
# Solution: https://www.youtube.com/watch?v=fZXyxGTqlgQ