# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def balancedTree(root):
            if not root:
                return [True, 0] 

            left = balancedTree(root.left)
            right = balancedTree(root.right)

            Balanced = (abs((left[1] - right[1])) <= 1 and 
            (left[0] and right[0]))
                
            return [Balanced, 1 + max(left[1], right[1])]
        return balancedTree(root)[0]
            

        