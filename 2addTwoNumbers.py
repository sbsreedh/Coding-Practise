# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1=[]
        stack2=[]
        node1=l1
        node2=l2
        while node1:
            stack1.append(node1.val)
            node1=node1.next
        while node2:
            stack2.append(node2.val)
            node2=node2.next
        summ=0
        carry=0
        head=None
        while stack1 or stack2:
            num1=0
            num2=0
            if stack1:num1=stack1.pop()
            if stack2: num2=stack2.pop()
            summ=(num1+num2+carry)
            carry=summ//10
            
            node=ListNode(summ%10)
            
            node.next=head
            head=node
        if carry>0:
            node=ListNode(carry)
            node.next=head
            head=node
        return head
        
            
            
