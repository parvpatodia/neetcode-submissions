# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            
            # Base case: empty node has height 0
            if not node:
                return 0
            
            # Recursively find height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update the maximum diameter found so far
            # Path length passing through this node = left height + right height
            max_diameter = max(max_diameter, left_height + right_height)
            
            # Return height of this subtree to the parent
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return max_diameter



            


        