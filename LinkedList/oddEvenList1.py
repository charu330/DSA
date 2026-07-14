# 328. Odd Even Linked List
# with extra space


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if not head or not head.next:
            return head
        curr=head
        ll1=[]
        ll2=[]
        index=1
        while curr:
            if(index%2!=0):
                ll1.append(curr.val)
            else:
                ll2.append(curr.val)
            curr=curr.next
            index+=1
        temp=ListNode(ll1[0])
        curr1=temp
        for i in ll1[1:]:
            curr1.next=ListNode(i)
            curr1=curr1.next
        curr2=temp
        while curr2.next:
            curr2 = curr2.next

        
        for i in ll2[0:]:
            curr2.next = ListNode(i)
            curr2 = curr2.next
        return temp


        
