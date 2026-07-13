# 1721. Swapping Nodes in a Linked List


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Move fast pointer k-1 steps to find node1
        fast = head
        for _ in range(1, k):
            fast = fast.next
        
        # Save reference to the k-th node from the start
        node1 = fast
        
        # Step 2: Start slow at head, move both until fast hits the tail
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        # slow is now standing on the k-th node from the end
        node2 = slow
        
        # Step 3: Swap their values
        node1.val, node2.val = node2.val, node1.val
        
        return head

        
