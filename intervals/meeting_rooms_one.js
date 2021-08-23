var canAttendMeetings = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  let i = 1;

  while (i < intervals.length) {
    const list1 = intervals[i - 1];
    const list2 = intervals[i];

    // Check for overlaps, (start and end can equal)
    a_overlaps_b = list1[0] >= list2[0] && list1[0] < list2[1];
    b_overlaps_a = list2[0] >= list1[0] && list2[0] < list1[1];

    // Since there is an overlap, can't attend all meetings
    if (a_overlaps_b || b_overlaps_a) return false;

    i++;
  }

  return true;
};
