# 876. Middle of the Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        current=head
        while current:
            res.append(current)
            current=current.next
        n=len(res)
        if(n%2!=0):
            mid=(n-1)//2
        else:
            mid=n//2  
        return res[mid]
