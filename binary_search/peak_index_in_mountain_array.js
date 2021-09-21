// This variation of of binary search helps us find the peak
var peakIndexInMountainArray = function (arr) {
  let start = 0,
    end = arr.length - 1;

  while (start < end) {
    let mid = Math.floor((start + end) / 2);

    // end = mid because mid might be the largest value
    if (arr[mid] > arr[mid + 1]) end = mid;
    // otherwise mid + 1 since there is no way it can be the max
    else start = mid + 1;
  }

  return end;
};
