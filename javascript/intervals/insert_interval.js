var insert = function (intervals, newInterval) {
  intervals.push(newInterval);
  // Sorting by start time
  intervals.sort((a, b) => a[0] - b[0]);

  const merged = [];
  let start = intervals[0][0];
  let end = intervals[0][1];

  for (let i = 1; i < intervals.length; i++) {
    const interval = intervals[i];

    // Overlapping intervals, determine the higher end time
    if (interval[0] <= end) end = Math.max(end, interval[1]);
    // Non-overlapping intervals, we push a new interval in
    else {
      merged.push([start, end]);
      start = interval[0];
      end = interval[1];
    }
  }

  // Adding the last interval
  merged.push([start, end]);
  return merged;
};
