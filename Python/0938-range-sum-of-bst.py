# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        
        return ans
    
#         def dfs(node):
#             if not node:
#                 return
#             if low <= node.val <= high:
#                 self.ans += node.val
#             if node.val > low:
#                 dfs(node.left)
#             if node.val < high:
#                 dfs(node.right)
        
#         self.ans = 0
#         dfs(root)
#         return self.ans
                