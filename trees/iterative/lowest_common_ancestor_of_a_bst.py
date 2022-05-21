def lowestCommonAncestor(self, root, p, q):
    while root:
        if root.val > max(p.val, q.val):
            root = root.left # Want a smaller root that is between or equal to
        elif root.val < min(p.val, q.val):
            root = root.right # Want a bigger root that is between or equal to
        else:
            return root

# Time Complexity: O(n)
# Space Complexity: O(1)