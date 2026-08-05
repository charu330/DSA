# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# with Kadane algo

#Dp question

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        j=0
        sum=0
        maxsum=float('-inf')
        for i in range(len(nums)):
            sum=sum+nums[i]
            if(sum>maxsum):
                maxsum=sum
            if(sum<0):
                sum=0
        return maxsum
        
