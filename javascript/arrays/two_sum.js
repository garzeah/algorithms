var twoSum = function (nums, target) {
  const indexMap = {};

  for (let i = 0; i < nums.length; i++) {
    const currentIndexVal = indexMap[nums[i]];

    // If we have the other pair in our map then we found the target
    if (currentIndexVal >= 0) return [currentIndexVal, i];
    else {
      // Storing the num we want to find on our map
      const numberToFind = target - nums[i];
      indexMap[numberToFind] = i;
    }
  }

  return null;
};
