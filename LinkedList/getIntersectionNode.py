# 160. Intersection of Two Linked Lists



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
            
        ptr1 = headA
        ptr2 = headB
        
        # Loop continues until both pointers point to the exact same node object
        while ptr1 != ptr2:
            # If ptr1 reaches the end, switch to headB; otherwise, move to next
            ptr1 = ptr1.next if ptr1 else headB
            
            # If ptr2 reaches the end, switch to headA; otherwise, move to next
            ptr2 = ptr2.next if ptr2 else headA
            
        # Both pointers will either meet at the intersection node, 
        # or both will become None at the same time if there is no intersection.
        return ptr1
