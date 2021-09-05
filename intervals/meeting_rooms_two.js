var minMeetingRooms = function (intervals) {
  let rooms = 0;
  let end = 0;

  // Getting the start and end times sorted
  const starts = intervals.map((a) => a[0]).sort((a, b) => a - b);
  const ends = intervals.map((a) => a[1]).sort((a, b) => a - b);

  for (let i = 0; i < intervals.length; i++) {
    // If there is a meeting that has ended by the time
    // the meeting at `start_pointer` starts
    if (ends[end] > starts[i]) rooms++;
    // Otherwise, we have an overlap
    else end++;
  }

  return rooms;
};
