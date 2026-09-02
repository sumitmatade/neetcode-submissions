# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0) # [rob_this_node, without_robbing_this_node]
            
            # Post-order traversal: process children first
            left_pair = dfs(node.left)
            right_pair = dfs(node.right)
            
            # Case 1: We rob this node. We CANNOT rob its direct children.
            with_node = node.val + left_pair[1] + right_pair[1]
            
            # Case 2: We DON'T rob this node. We can either rob or not rob its children.
            # We take the maximum of either choice for both the left and right child.
            without_node = max(left_pair) + max(right_pair)
            
            return (with_node, without_node)
            
        return max(dfs(root))