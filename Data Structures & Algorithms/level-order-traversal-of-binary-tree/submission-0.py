# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ##Understand
        '''
        given the root of a binary tree (which is going to have left and right subtrees), our job is to return the level order traversal of the tree in a list where each sublist is a the level of the tree. 

        can our tree ever be empty and if it is empty, what can we return? 
        empty -> []
        '''

        ##Match
        '''
        since we want a level order traversal, this would be perfect for a bfs algorithm where we can through each level and capture the values of the nodes in that level
        '''

        if not root:
            return []
        
        q = deque()

        q.append(root)

        res = []

        while q:
            qlen = len(q)
            sublist = []
            for _ in range(qlen):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sublist.append(node.val)
            res.append(sublist)
        return res
                