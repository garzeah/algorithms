var findMin = function (nums) {
  let start = 0,
    end = nums.length - 1;

  while (start < end) {
    let mid = Math.floor((start + end) / 2);

    // This allows us to find the minimum, if the switch
    // to <, then we can find the max
    if (nums[mid] > nums[end]) start = mid + 1;
    else end = mid;
  }

  return nums[start];
};
