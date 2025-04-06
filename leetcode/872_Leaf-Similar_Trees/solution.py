# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves = []
        stack = deque()

        stack.append(root1)

        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.val)
                continue
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        stack.append(root2)
        i = 0
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if i >= len(leaves) or leaves[i] != node.val:
                    return False
                i += 1
                continue
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return i == len(leaves)
