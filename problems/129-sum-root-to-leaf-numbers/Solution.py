from TreeNode import TreeNode

class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        total = ""
        
        def dfs(root, total):
          
          if root:
          
            if root.left is None and root.rigth is None:
                return int(total + str(root.val))
            
            total+= str(root.val)
            return dfs(root.left, total) + dfs(root.rigth, total)
          
          else:
            return 0
        
        return dfs(root, total)
                    