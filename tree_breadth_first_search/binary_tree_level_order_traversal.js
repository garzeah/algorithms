var levelOrder = function (root) {
  if (root === null) return [];

  const queue = [];
  const data = [];
  queue.push(root);

  while (queue.length > 0) {
    const levelSize = queue.length;
    currentLevel = [];
    for (i = 0; i < levelSize; i++) {
      currentNode = queue.shift();

      // Add the node to the current level
      currentLevel.push(currentNode.val);

      // Insert the children of current node in the queue
      if (currentNode.left !== null) queue.push(currentNode.left);
      if (currentNode.right !== null) queue.push(currentNode.right);
    }
    data.push(currentLevel);
  }

  return data;
};
