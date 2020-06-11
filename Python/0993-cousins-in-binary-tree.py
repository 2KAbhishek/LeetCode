# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def getNodeInfo(node: TreeNode, parent : TreeNode, level : int):

            if not node or len(res) == 2:
                return
            else:
                if node.val == x or node.val == y:
                    res.append((level, parent))

                return getNodeInfo(node.left, node, level+1) or getNodeInfo(node.right, node, level+1)

        res = []
        getNodeInfo(root, None, 1)

        return res[0][0] == res[1][0] and res[0][1] != res[1][1]

