# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(root, arr, n, index): 

            if (root == None): return False
            
            if root.left == None and root.right == None and root.val == arr[index] and index == n - 1:
                return True
            
            if index < n-1 and root.val == arr[index]:
                return dfs(root.left, arr, n, index+1) or dfs(root.right, arr, n, index+1)
            
        n = len(arr)
        return dfs(root, arr, n, 0)
            