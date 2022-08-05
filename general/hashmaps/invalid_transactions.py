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
        invalid = []

        # Record all transactions done at a particular time
        # including the person and the location.
        transaction_time = defaultdict(dict)
        for transaction in transactions:
            name, str_time, amount, city = transaction.split(",")
            time = int(str_time)

            if name not in transaction_time[time]:
                transaction_time[time][name] = [city]
            else:
                transaction_time[time][name].append(city)

        for transaction in transactions:
            name, str_time, amount, city = transaction.split(",")
            time = int(str_time)

            # Check amount
            if int(amount) > 1000:
                invalid.append(transaction)
                continue

            # Check if person did transaction within 60 minutes in a different city
            start_time = max(0, int(time) - 60)
            end_time = max(0, int(time) + 61)
            for invalid_time in range(start_time, end_time):
                if invalid_time not in transaction_time:
                    continue

                # Invalid time does not belong to this person's transaction
                if name not in transaction_time[invalid_time]:
                    continue

                # Getting cities associated with this person's transaction
                cities = transaction_time[invalid_time][name]

                # Checking if transactions were done in a different city within
                # a 1 hour timeframe or checking if there are duplicate transactions
                if city not in cities or len(cities) > 1:
                    invalid.append(transaction)
                    break

        return invalid

# Time Complexity: O(n) would be our worst case scenario since we only iterate
# through a transaction at most only 1 time. If we were to do brute force, we
# would have to compare each transaction with every other transaction as we
# iterate through our array.

# Space Complexity: O(n) where n is the amount of of transactions we have.

# Solution: https://leetcode.com/problems/invalid-transactions/discuss/1570056/O(N)-using-HashTableHashMap-or-Comments-added
