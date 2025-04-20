# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.deleteNodeHelper(root, key)

    def deleteNodeHelper(self, node, key):
        if node is None:
            return node
        elif key < node.val:
            node.left = self.deleteNodeHelper(node.left, key)
        elif key > node.val:
            node.right = self.deleteNodeHelper(node.right, key)
        else:
            if not node.left and not node.right:
                node = None
            elif node.right:
                node.val = self.successor(node)
                node.right = self.deleteNodeHelper(node.right, node.val)
            else:
                node.val = self.predecessor(node)
                node.left = self.deleteNodeHelper(node.left, node.val)
        return node

    def predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val
