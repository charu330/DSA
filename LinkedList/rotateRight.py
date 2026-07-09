# 61. Rotate List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        k=k%count
        if k==0:
            return head
        slow=head
        fast=head
        for _ in range(k):
            fast=fast.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        new_head=slow.next
        slow.next=None
        fast.next=head
        return new_head


        
