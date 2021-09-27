class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const traverse = function (root) {
  const result = [];
  if (!root) return result;

  // Initializing our queue
  const queue = [root];

  while (queue.length > 0) {
    // Getting the size of each tree level
    const levelSize = queue.length;
    const level = [];

    for (let i = 0; i < levelSize; i++) {
      // Add the node to the current level
      let currNode = queue.shift();
      level.push(currNode.value);

      // Insert the children of current node in the queue
      if (currNode.left) queue.push(currNode.left);
      if (currNode.right) queue.push(currNode.right);
    }

    // Add to the beginning of the array to get reverse order
    result.unshift(level);
  }

  return result;
};

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
console.log(`Reverse level order traversal: ${traverse(root)}`);
