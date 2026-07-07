# 1290. Convert Binary Number in a Linked List to Integer


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans=0
        current= head
        while current:
            ans=ans*2+current.val
            current=current.next
        return ans
        
        
