const make_squares = function(arr) {
  const squares = [];
  let left = 0, right = arr.length - 1, highestSquareIdx = arr.length - 1;

  while (left <= right) {
    let leftSquare = arr[left] * arr[left],
      rightSquare = arr[right] * arr[right];

    if (leftSquare > rightSquare) {
      squares[highestSquareIdx] = leftSquare;
      left++;
    // If right is greater or equal then assign we will assign the number to this
    // position in the squares array
    } else {
      squares[highestSquareIdx] = rightSquare;
      right--;
    }

    highestSquareIdx--;
  }

  return squares;
};