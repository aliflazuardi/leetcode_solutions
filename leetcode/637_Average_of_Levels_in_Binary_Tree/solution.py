# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()

        q.append((0, root))
        ans = []
        level_sum = 0
        level_count = 0
        curr_level = 0

        while q:
            level, node = q.popleft()
            if level != curr_level:
                ans.append(level_sum / level_count)
                curr_level = level
                level_sum = 0
                level_count = 0
            level_sum += node.val
            level_count += 1
            if node.left:
                q.append((curr_level + 1, node.left))
            if node.right:
                q.append((curr_level + 1, node.right))

        ans.append(level_sum / level_count)

        return ans
