# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        else:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)

            root.left = right
            root.right = left
            return root

        return (self.invertTree(root))

