const find_missing_number = function (nums) {
  let i = 0;

  while (i < nums.length) {
    const j = nums[i];

    if (nums[i] !== nums[j]) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
    } else {
      i++;
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== i) return i;
  }
};
