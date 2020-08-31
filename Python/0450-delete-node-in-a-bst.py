# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            # The snallest node int the right subtree replaces root
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            root.val = tmp.val

            root.right = self.deleteNode(root.right, tmp.val)

            # The liargest node int the right subtree replaces root
#             tmp = root.left
#             while tmp.right:
#                 tmp = tmp.right
#             root.val = tmp.val

#             root.left = self.deleteNode(root.left, tmp.val)

        return root

