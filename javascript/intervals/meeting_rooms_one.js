var canAttendMeetings = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0]);

  for (let i = 1; i < intervals.length; i++) {
    // If the end is greater than the start then there is an overlap
    if (intervals[i - 1][1] > intervals[i][0]) return false;
  }

  return true;
};
