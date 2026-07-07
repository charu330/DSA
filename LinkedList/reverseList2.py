# 206. Reverse Linked List


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  # 1. Save the next node
            curr.next = prev  # 2. Reverse the current node's pointer
            prev = curr       # 3. Move prev forward
            curr = nxt        # 4. Move curr forward
            
        # prev will be pointing to the new head of the reversed list
        return prev


        
