# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = deque()

        stack.append((root, root.val))
        count = 0

        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                count += 1
                max_val = node.val

            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))

        return count
