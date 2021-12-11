var sortColors = function (nums) {
  const swap = (i, j) => ([nums[i], nums[j]] = [nums[j], nums[i]]);

  let current = 0,
    left = 0;
  let right = nums.length - 1;

  while (current <= right) {
    // Swap to pos. of left pointer
    if (nums[current] === 0) {
      swap(left, current);
      left++;
      current++;
      // Swap to pos. of right pointer
    } else if (nums[current] === 2) {
      swap(right, current);
      right--;
      // Increment the current index
    } else {
      current++;
    }
  }

  return nums;
};
