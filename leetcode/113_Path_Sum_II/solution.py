# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        ans = []
        stack = deque()
        stack.append((root, [root.val]))

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                if sum(path) == targetSum:
                    ans.append(path)
                continue

            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if node.left:
                stack.append((node.left, path + [node.left.val]))

        return ans
