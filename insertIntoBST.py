# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TC:O(H), H-height of the BST
#SC:O(H)

#recursive Solution:
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val<=root.val:
            root.left=self.insertIntoBST(root.left,val)
        else :
            root.right=self.insertIntoBST(root.right,val)
        return root
        
        
#Iterative Solution:
#TC:O(H), H-height of the BST
#SC:O(1)
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        if root:
            curr=root
            prev=None
            while curr:
                prev=curr
                if val<=prev.val:
                    curr=prev.left
                else:
                    curr=prev.right
            if val<=prev.val:
                prev.left=TreeNode(val)
            else:
                prev.right=TreeNode(val)
            return root
        else:
            return TreeNode(val)


        
