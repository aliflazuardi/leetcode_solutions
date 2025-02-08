# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return dfs(root, 0)


def dfs(root, depth):
    if root is None:
        return depth

    dl = dfs(root.left, depth + 1)
    dr = dfs(root.right, depth + 1)

    return max(dl, dr)
