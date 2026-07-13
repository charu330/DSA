# 92. Reverse Linked List II



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        prev=None
        curr=head
        for _ in range(1, left):
            prev = curr
            curr = curr.next
        before_sublist = prev
        sublist_tail = curr
        for _ in range (left, right+1):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        if before_sublist:
            before_sublist.next = prev
        sublist_tail.next = curr
        return prev if left == 1 else head
