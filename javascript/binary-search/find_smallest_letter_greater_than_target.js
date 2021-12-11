var nextGreatestLetter = function (letters, key) {
  let start = 0,
    end = letters.length - 1;

  while (start <= end) {
    mid = Math.floor(start + (end - start) / 2);
    if (key < letters[mid]) end = mid - 1;
    else start = mid + 1;
  }

  // Since the loop is running until 'start <= end',
  // so at the end of the while loop, 'start === end+1'
  return letters[start % letters.length];
};
