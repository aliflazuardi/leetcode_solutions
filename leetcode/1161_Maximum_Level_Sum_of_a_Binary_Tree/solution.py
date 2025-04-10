# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        level_sum = []
        queue.append((root, 0))

        max_sum = -sys.maxsize - 1
        max_level = 0
        while queue:
            node, level = queue.popleft()

            if len(level_sum) == level:
                level_sum.append(node.val)
                if level != 0 and level_sum[level - 1] > max_sum:
                    max_sum = level_sum[level - 1]
                    max_level = level
            else:
                level_sum[level] += node.val

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        if level_sum[-1] > max_sum:
            max_level = len(level_sum)

        return max_level
