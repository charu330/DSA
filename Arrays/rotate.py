# 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# By reversal of array and in place rotation

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
        self.reverse(nums, 0, len(nums)-k-1)
        self.reverse(nums,len(nums)-k, len(nums)-1)
        self.reverse(nums,0, len(nums)-1)
    
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while(start<end):
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
        
    
