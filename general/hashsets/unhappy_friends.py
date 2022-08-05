class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # The goal is to find everyone that prefers each other over their
        # current partner, if that's the case then they are an unhappy
        # friend. We can do this by creating a hashset of a person and
        # a set of everyone they prefer over their current partner.
        # Then we can check through every person and for everyone
        # they prefer, check if they are in the preferee's list
        # of people they prefer

        prefs = {} # person : set{ everyone they prefer over current partner }

        # Want to get a set of people that x and u prefer
        # over their current partner
        for (x, u) in pairs:
            prefs[x] = set()
            prefs[u] = set()

            # Want to find who x prefers over current partner
            for person in preferences[x]:
                # Break since we only want to get the people
                # they prefer over their current partner
                if person == u:
                    break

                prefs[x].add(person)

            # Want to find who u prefers over current partner
            for person in preferences[u]:
                # Break since we only want to get the people
                # they prefer over their current partner
                if person == x:
                    break

                prefs[u].add(person)

        # For every person who prefers someone else over their current partner
        # and for every preferee (a person that someone prefers over their
        # current partner), we want to check if that is in that preferee's
        # list of ppl they prefer over their current partner since that
        # preferee is already in that person's list of ppl they prefer
        res = 0
        for person in prefs:
            for preferee in prefs[person]:
                if person in prefs[preferee]:
                    res += 1
                    break

        return res


# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=10laHayu2dc