
class UndergroundSystem:

    def __init__(self):
        self.checkedInCustomers = {} # id : (stationName, t)
        self.tripTimes = {} # (startStation, stationName) : [tripTime, numberOfTrips]

    # Checking in a customer
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedInCustomers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkedInCustomers[id]
        del self.checkedInCustomers[id]
        tripTime = t - startTime

        # Recording the trip duration and number of trips for the first time
        if (startStation, stationName) not in self.tripTimes:
            self.tripTimes[(startStation, stationName)] = [tripTime, 1]
        else: # If we already have this station pair, add to the tripTime and numberOfTrips
            self.tripTimes[(startStation, stationName)][0] += tripTime
            self.tripTimes[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        sumOfTimes, numberOfTrips = self.tripTimes[(startStation, endStation)]

        return sumOfTimes / numberOfTrips



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# Time Complexity:
#   - checkIn(id, stationName, t): O(1)
#   - checkOut(id, stationName, t): O(1)
#   - getAverageTime(startStation, endStation): O(1), it is good to aim for a TC
# of O(1) because we are most likely going to display this data on a dashboard
# screen that'll constantly refresh. We want to be as optimal as we can.

# Space Complexity: O(n) where n is the amount of people checked in a given moment.

# Solution: https://leetcode.com/problems/design-underground-system/discuss/1976766/Python-or-Two-dictionaries-or-Simple-and-Short