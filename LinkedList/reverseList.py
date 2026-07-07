# 206. Reverse Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        stack=[]
        if not head:
            return None
        while current:
            stack.append(current)
            current=current.next
        new_head = stack.pop()
        current = new_head
        for i in range(len(stack)-1, -1, -1):
            current.next= stack[i]
            current=current.next
        current.next=None
        return new_head


        
