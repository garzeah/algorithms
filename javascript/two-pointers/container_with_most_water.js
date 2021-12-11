var maxArea = function (height) {
  let left = 0,
    right = height.length - 1,
    result = -Infinity;

  while (left < right) {
    // Calculate minimum length between 2 values so water does not overflow
    minLength = Math.min(height[left], height[right]);
    width = right - left;

    // Calculating the max area with each iteration
    result = Math.max(result, minLength * width);

    if (height[left] < height[right]) left++;
    else right--;
  }

  return result;
};
