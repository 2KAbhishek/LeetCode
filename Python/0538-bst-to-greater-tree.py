# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root, total):
            if root is None: return 0

            rightVal = dfs(root.right, total)
            leftVal = dfs(root.left, total + root.val + rightVal)
            ret = rightVal + leftVal + root.val
            root.val += total + rightVal
            return ret

        dfs(root, 0)
        return root

