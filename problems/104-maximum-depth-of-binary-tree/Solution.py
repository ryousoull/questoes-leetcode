from TreeNode import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
          return 0
        left = self.maxDepth(root.left)
        rigth = self.maxDepth(root.right)
        return 1 + max(left, rigth)