var groupAnagrams = function (strs) {
  const obj = {};

  for (let str of strs) {
    // Split each string, sort letters, and join
    let letters = str.split("").sort().join("");

    // For each freq., we want to push the original string
    // if it exists or create an array w/ the string
    obj[letters] ? obj[letters].push(str) : (obj[letters] = [str]);
  }

  return Object.values(obj);
};
