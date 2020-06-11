# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return None
        if val == root.val: return root
        l = self.searchBST(root.left, val)
        r = self.searchBST(root.right, val)
        if l: return l
        return r

