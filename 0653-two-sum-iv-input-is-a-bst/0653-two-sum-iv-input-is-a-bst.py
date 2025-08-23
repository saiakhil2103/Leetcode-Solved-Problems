# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        elements=[]
        def iterate(root):
            if root:
                iterate(root.left)
                elements.append(root.val)
                iterate(root.right)
        iterate(root)
        start=0
        end=len(elements)-1
        while start<end:
            if elements[start]+elements[end]==k:
                return True
            elif elements[start]+elements[end]<k:
                start+=1
            else:
                end-=1
        return False