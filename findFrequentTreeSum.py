# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Bottom up DFS solution 
#TC:O(h)
#SC:O(v)

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def helper(root):
            s=root.val
            if root.right:
                s+=helper(root.right)
            if root.left:
                s+=helper(root.left)
            hashMap[s]+=1
            return s
        if not root:
            return []
        hashMap=defaultdict(int)
        helper(root)
        maxsum=max(hashMap.values())
        return [x for x in hashMap if hashMap[x]==maxsum]
        
