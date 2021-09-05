const search_ceiling_of_a_number = function (arr, key) {
  let start = 0;
  let end = arr.length - 1;

  // If the 'key' is bigger than the biggest element
  if (key > arr[arr.length - 1]) return -1;

  while (start <= end) {
    let middle = Math.floor((start + end) / 2);
    if (key < arr[middle]) end = middle - 1;
    else if (key > arr[middle]) start = middle + 1;
    else return middle;
    console.log(`Start: ${start}, Middle: ${middle}, End: ${end}`);
  }

  // Since the loop is running until 'start <= end',
  // so at the end of the while loop, 'start === end+1'
  // we are not able to find the element in the given
  // array, so the next big number will be arr[start]
  return start;
};

console.log(search_ceiling_of_a_number([4, 6, 10], 6));
console.log(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12));
console.log(search_ceiling_of_a_number([1, 3, 8, 10, 15], 7));
console.log(search_ceiling_of_a_number([4, 6, 10], 17));
console.log(search_ceiling_of_a_number([4, 6, 10], -1));
