const leftMax = [],
  rightMax = [],
  minWallHeights = [];
let currLeftMax = 0,
  currRightMax = 0;
let total = 0;

// Finding the left max of walls for each pos.
for (let i = 0; i < height.length; i++) {
  currLeftMax = Math.max(currLeftMax, height[i]);
  leftMax.push(currLeftMax);
}

// Finding the right max of walls for each pos.
for (let i = height.length - 1; i >= 0; i--) {
  currRightMax = Math.max(currRightMax, height[i]);
  rightMax.unshift(currRightMax);
}

// Finding the min wall heights between leftMax and rightMax
for (let i = 0; i < height.length; i++) {
  let currLeft = leftMax[i];
  let currRight = rightMax[i];
  let minWallHeight = Math.min(currLeft, currRight);

  minWallHeights.push(minWallHeight);
}

// Calculating the water height
for (let i = 0; i < height.length; i++) {
  let currHeight = height[i];
  let minWallHeight = minWallHeights[i];
  let currWaterHeight = minWallHeight - currHeight;

  // minWallHeight - currHeight gives us the water level
  if (currWaterHeight <= 0) continue;
  else total += currWaterHeight;
}

return total;
