def lowestCommonAncestor(self, root, p, q):
    while root:
        # We want to check for a smaller LCA
        if root.val > p.val and root.val > q.val:
            root = root.left
        # Want to check for a bigger LCA
        elif root.val < p.val and root.val < q.val:
            root = root.right
        # They are equal or in between meaning we found the BST
        else:
            return root

# Time Complexity: O(n)
# Space Complexity: O(1)