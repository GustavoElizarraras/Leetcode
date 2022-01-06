# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        tree = [root] if root else []
        while tree:
            depth += 1
            queue = []
            for node in tree:
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            tree = queue
        return depth
        
        