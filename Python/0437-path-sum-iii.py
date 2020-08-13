# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        hm = defaultdict(int)    
        
        def dfs(node, prefixsum, target):
            paths = 0
            if not node:
                return paths
            prefixsum += node.val
            if prefixsum == target:
                paths += 1
            paths += hm[prefixsum - target]
            hm[prefixsum] += 1
            paths += dfs(node.left, prefixsum, target)
            paths += dfs(node.right, prefixsum, target)
            hm[prefixsum] -= 1
            return paths
        
        return dfs(root, 0, sum)
    