#https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Height(self, root: Optional[TreeNode]) -> bool:
        #if we reach the end, return 0
        if root is None:
            return 0
        
        #recursive call
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)

        #if the difference between the heights is more than 1 or the same is true down the line,
        #return -1
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1

        #the height of this node is the maximum or its left and right trees
        return max(leftheight, rightheight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.Height(root) >= 0