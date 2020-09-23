# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#TC:O(n)
#SC:O(n)
#recursive solution
class Solution:
  
    def convertBST(self, root):
        self.total = 0
        def helper(root):
            if root is not None:
                helper(root.right)
                self.total += root.val
                root.val = self.total
                helper(root.left)
            return root

            
        return helper(root)
#Iterative Solution      
class Solution:
  
    def convertBST(self, root):
        total=0
        node=root
        stack=[]
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node=node.right
            node=stack.pop()
            total+=node.val
            node.val=total
        
            node=node.left
        return root
        
