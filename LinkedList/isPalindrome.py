# 234. Palindrome Linked List



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or head.next==None:
            return True
        curr=head
        stk=[]
        while curr:
            stk.append(curr.val)
            curr=curr.next
        if stk==stk[::-1]:
            return True
        else:
            return False
        
