# 1721. Swapping Nodes in a Linked List



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        current=head
        n=0
        while current:
            n+=1
            current=current.next
        
        node1=head
        
        for _ in range(1,k):
            node1=node1.next
        node2=head
        for _ in range(1, n-k+1):
            node2=node2.next
        temp = node1.val
        node1.val = node2.val
        node2.val = temp

        return head
            
        
