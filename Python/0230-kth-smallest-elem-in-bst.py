# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
#         def inorder(root):
#             if not root:
#                 return out

#             inorder(root.left)
#             out.append(root.val)
#             inorder(root.right)

#         out = []
#         inorder(root)
#         return out[k - 1]

        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

