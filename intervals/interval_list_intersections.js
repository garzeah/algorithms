var intervalIntersection = function (firstList, secondList) {
  const intersect = [];
  let i = 0,
    j = 0;

  while (i < firstList.length && j < secondList.length) {
    // If the start of A is between the intervals of B, then A overlaps B
    a_overlaps_b =
      firstList[i][0] >= secondList[j][0] &&
      firstList[i][0] <= secondList[j][1];

    // If the start of B is between the intervals of A, then B overlaps A
    b_overlaps_a =
      secondList[j][0] >= firstList[i][0] &&
      secondList[j][0] <= firstList[i][1];

    // If we have an overlap, push the intersect by finding max of X and min of Y
    if (a_overlaps_b || b_overlaps_a) {
      intersect.push([
        Math.max(firstList[i][0], secondList[j][0]),
        Math.min(firstList[i][1], secondList[j][1])
      ]);
    }

    // We want to throw away the shorter end of the interval since we don't need it anymore
    if (firstList[i][1] < secondList[j][1]) i++;
    else j++;
  }

  return intersect;
};
