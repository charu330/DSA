
# 234. Palindrome Linked List
# through two pointer and extra space


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. Extract values into a standard array
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
            
        # 2. Use two pointers to verify the palindrome
        left = 0
        right = len(values) - 1
        
        while left < right:
            if values[left] != values[right]:
                return False  # Mismatch found, not a palindrome
            left += 1         # Move forward
            right -= 1        # Move backward
            
        return True

        
