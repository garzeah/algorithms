var peakIndexInMountainArray = function (nums) {
  if (nums.length === 1) return 0;
  let start = 0,
    end = nums.length - 1;

  while (start <= end) {
    let mid = start + Math.floor((end - start) / 2);

    if (nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1]) return mid;
    else if (nums[mid] < nums[mid - 1]) end = mid - 1;
    else if (nums[mid] < nums[mid + 1]) start = mid + 1;
  }
  return -1;
};
