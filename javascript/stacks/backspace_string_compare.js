var backspaceCompare = function (s, t) {
  var handleBackspace = function (str) {
    const stack = [];
    let i = 0;

    while (i < str.length) {
      if (str[i] === "#") stack.pop();
      else stack.push(str[i]);
      i++;
    }

    return stack.join("");
  };

  return handleBackspace(s) === handleBackspace(t);
};
