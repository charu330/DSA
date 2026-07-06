

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res=[]
        s=""
        current= head
        while current:
            s+=str(current.val)
            current=current.next
        integer_val = int(s, 2)
        return integer_val
        
        