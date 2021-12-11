var firstMissingPositive = function (nums) {
  let i = 0;
  const n = nums.length;

  while (i < n) {
    const j = nums[i] - 1;
    if (nums[i] !== nums[j]) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
    } else i++;
  }

  for (let i = 0; i < n; i++) {
    if (nums[i] !== i + 1) return i + 1;
  }

  // Returning length of array, cyclic sort
  // might've changed the size of original
  return n + 1;
};
