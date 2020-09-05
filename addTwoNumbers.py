#TC:O(N)
#SC:O(1)




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=None
        ptr1=l1
        ptr2=l2
        carry=0
        dummy_head=ListNode(0);
        temp=dummy_head;
        while l1 or l2:
            a=0
            b=0
            if l1:
                a=l1.val
                l1=l1.next
            if l2:
                b=l2.val
                l2=l2.next
            
            currSum=a+b+carry
            carry=currSum//10
            node=ListNode(currSum%10)
            temp.next=node
            temp=temp.next
        if carry>0:
            node=ListNode(carry)
            temp.next=node
            temp=temp.next
        return dummy_head.next
            
            
            
        
            
        
            
