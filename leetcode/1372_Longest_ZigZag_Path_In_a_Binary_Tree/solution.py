# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return dfs(root, 0, 0)


def dfs(node, l_c, r_c):
    if node.left:
        l_c = dfs(node.left, 0, l_c + 1)
    if node.right:
        r_c = dfs(node.right, r_c + 1, 0)

    return max(l_c, r_c)
