# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
       
        seen = set()
        max_k = -1
        
        for num in nums:
            # Check if the negative counterpart has already been seen
            if -num in seen:
                max_k = max(max_k, abs(num))
            seen.add(num)
            
        return max_k
