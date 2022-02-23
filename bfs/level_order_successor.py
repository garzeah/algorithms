from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  if root is None:
    return None

  queue = deque()
  queue.append(root)

  while queue:
    curr_node = queue.popleft()
    # Insert the children of current node in the queue
    if curr_node.left:
      queue.append(curr_node.left)
    if curr_node.right:
      queue.append(curr_node.right)

    # Break if we have found the key
    if curr_node.val == key:
      break

  # Return the first value in the queue since
  # that will be the next level order successor
  return queue[0] if queue else None


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()

# Time Complexity: O(n)
# Space Complexity: O(n)