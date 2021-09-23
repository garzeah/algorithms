class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

function traverse(root) {
  if (root === null) return result;
  const result = [];

  // Initializing our queue
  const queue = [root];

  while (queue.length > 0) {
    // Getting the size of each tree level
    const levelSize = queue.length;
    const currentLevel = [];

    for (i = 0; i < levelSize; i++) {
      currentNode = queue.shift();
      // Add the node to the current level
      currentLevel.push(currentNode.val);

      // Insert the children of current node in the queue
      if (currentNode.left !== null) queue.push(currentNode.left);
      if (currentNode.right !== null) queue.push(currentNode.right);
    }

    result.push(currentLevel);
  }

  return result;
}

const root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
console.log(`Level order traversal: ${traverse(root)}`);
