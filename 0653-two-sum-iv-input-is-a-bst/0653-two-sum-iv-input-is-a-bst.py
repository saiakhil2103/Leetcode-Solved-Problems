# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited_elements=set()
        def dfs(root):
            if root:
                if k-root.val in visited_elements:
                    return True
                visited_elements.add(root.val)
                return dfs(root.left) or dfs(root.right)
            return False
        return dfs(root)