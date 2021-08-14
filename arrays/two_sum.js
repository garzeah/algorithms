var twoSum = function (nums, target) {
  const numsMap = {};

  for (let i = 0; i < nums.length; i++) {
    const currentMapVal = numsMap[nums[i]];

    // If we have the other pair in our map then we found the target
    if (currentMapVal >= 0) return [currentMapVal, i];
    else {
      // Storing the num we want to find on our map
      const numberToFind = target - nums[i];
      numsMap[numberToFind] = i;
    }
  }

  return null;
};
