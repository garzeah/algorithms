intervals.sort((a, b) => a[1] - b[1]);

let prevInterval = intervals[0];
let counter = 0;

for (let i = 1; i < intervals.length; i++) {
  // Since we sorted by end times if the end
  // is greater than the start then we add
  // to our counter
  if (prevInterval[1] > intervals[i][0]) counter++;
  // Otherwise, we'll move it up and check the others
  else prevInterval = intervals[i];
}
return counter;
