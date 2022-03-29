def find_path(root, sequence):
    if root is None:
        return len(sequence) == 0

    return find_path_recursive(root, sequence, 0)


def find_path_recursive(curr_node, sequence, sequence_idx):
    if curr_node is None:
        return False

    seq_len = len(sequence)
    if sequence_idx >= seq_len or curr_node.val != sequence[sequence_idx]:
        return False

    # If the current node is a leaf, add it is the end of the sequence, we have found a path!
    if curr_node.left is None and curr_node.right is None and sequence_idx == seq_len - 1:
        return True

    # Recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return find_path_recursive(curr_node.left, sequence, sequence_idx + 1) or \
        find_path_recursive(curr_node.right, sequence, sequence_idx + 1)

# Time Complexity: The time complexity of the above algorithm is O(N),
# where ‘N’ is the total number of nodes in the tree. This is due to
# the fact that we traverse each node once.

# Space Complexity: The space complexity of the above algorithm will O(N) in
# the worst case. This space will be used to store the recursion stack. The
# worst case will happen when the given tree is a linked
# list (i.e., every node has only one child).