# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -math.inf
        def dfs(node):
            nonlocal maxSum
            if node == None:
                return -math.inf
            left = dfs(node.left)
            right = dfs(node.right)
            #print(left, node.val, right)
            totalMax = max([left, right, left + node.val, right + node.val, left + node.val + right, node.val])
            if (totalMax > maxSum):
                maxSum = totalMax
            #must be conected to curnode to see next
            #print('return', max([left + node.val, right + node.val, node.val]))
            return max([left + node.val, right + node.val, node.val])
        dfs(root)
        return maxSum