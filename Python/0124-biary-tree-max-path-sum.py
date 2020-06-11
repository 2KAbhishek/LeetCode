# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int: 
        
        def pathSum(node: TreeNode) -> int:
            if not node: return 0
            left = max(0, pathSum(node.left))
            right = max(0, pathSum(node.right))
            self.maxSum = max(self.maxSum, left + right + node.val)
            return max(left, right) + node.val
        
        self.maxSum = float(-inf)
        pathSum(root)
        return self.maxSum
    