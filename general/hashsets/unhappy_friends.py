class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # The goal is to find everyone that prefers each other over their
        # current partner, if that's the case then they are an unhappy
        # friend. We can do this by creating a hashset of a person and
        # a set of everyone they prefer over their current partner.
        # Then we can check through every person and for everyone
        # they prefer, check if they are in the preferee's list
        # of people they prefer

        preferred = {} # person : set{ everyone they prefer over current partner }

        # Want to store everyone they prefer over their current partner
        for (x, y) in pairs:
            preferred[x] = set()
            preferred[y] = set()

            for person in preferences[x]:
                if person == y:
                    break

                preferred[x].add(person)

            for person in preferences[y]:
                if person == x:
                    break

                preferred[y].add(person)

        # For every person that prefers someone else and for every preferee in that
        # person's list of people they prefer, if that person is in that preferee's
        # list of people they prefer, then we have an unhappy friend
        res = 0
        for person in preferred:
            for preferee in preferred[person]:
                if person in preferred[preferee]:
                    res += 1
                    break

        return res

# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=10laHayu2dc