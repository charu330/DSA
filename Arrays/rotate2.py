# 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# By python slicing and inplace rotation

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return None
        if k>=len(nums):
            k=k%len(nums)
        if(k<0):
            k=k+len(nums)
        nums[:]= nums[-k:]+ nums[:-k]
        
    
