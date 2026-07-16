# 19. Remove Nth Node From End of List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        prev=None
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        curr=head
        for _ in range(count-n):
            prev=curr
            curr=curr.next
        if prev is None:
            return head.next
        else:
            prev.next = curr.next
        return head
