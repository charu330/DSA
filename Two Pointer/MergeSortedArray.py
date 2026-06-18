# Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k=n
        for i in range((k)):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
        

        
