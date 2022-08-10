from collections import defaultdict

"""
https://www.notion.so/paulonteri/Hashtables-Hashsets-220d9f0e409044c58ec6c2b0e7fe0ab5#cf22995975274881a28b544b0fce4716
"""

class Solution(object):
    def invalidTransactions(self, transactions):
        """
        - Record all transactions done at a particular time. Recording the person and the location. Example:
            `['alice,20,800,mtv','bob,50,1200,mtv','bob,20,100,beijing']` :\n
            `
            {
                20: {'alice': ['mtv'], 'bob': ['beijing']},
                50: {'bob': ['mtv']}
            }
            `
            `{time: {person: [location], person2: [location1, location2]}, time: {person: [location]}}`
        - For each transaction, check if the amount is invalid - and add it to the invalid transactions if so.
        - For each transaction, go through invalid times (+-60), check if a transaction by the same person happened
            in a different city - and add it to the invalid transactions if so.
        """

        # Record all the transactions done at a particular
        # time, by a particular person and which cities at
        # which these transactions have occurred at
        times = defaultdict(dict) # { time: { name: { set of cities } } }

        for transaction in transactions:
            name, str_time, amount, city = transaction.split(",")
            time = int(str_time)

            # If a person's name doesn't exist, then we have to record
            # their name and where their transaction happened
            if name not in times[time]:
                times[time][name] = {city}
            # The name exists at this time so add their new city
            else:
                times[time][name].add(city)

        res = []
        for transaction in transactions:
            name, str_time, amount, city = transaction.split(",")
            time = int(str_time)

            # Check amount
            if int(amount) > 1000:
                res.append(transaction)
                continue

            # Check if person did transaction within 60 minutes in a different city
            start, end = max(0, time - 60), max(0, time + 61)
            for time in range(start, end):
                # There is no transaction occurring at this time
                if time not in times:
                    continue

                # This person is not associated with this transaction
                if name not in times[time]:
                    continue

                # Getting cities associated with this person's transaction
                cities = times[time][name]

                # Checking if transactions were done in a different
                # city within a 1 hour timeframe
                if city not in cities or len(cities) > 1:
                    res.append(transaction)
                    break

        return res

# Time Complexity: O(n) would be our worst case scenario since we only iterate
# through a transaction at most only 1 time. If we were to do brute force, we
# would have to compare each transaction with every other transaction as we
# iterate through our array.

# Space Complexity: O(n) where n is the amount of of transactions we have.

# Solution: https://leetcode.com/problems/invalid-transactions/discuss/1570056/O(N)-using-HashTableHashMap-or-Comments-added
