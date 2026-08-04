# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# Solution with 2 pass approach

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_0=0
        count_1=0
        count_2=0
        for i in range(len(nums)):
            if(nums[i]==0):
                count_0+=1
            if(nums[i]==1):
                count_1+=1
            if(nums[i]==2):
                count_2+=1
        for i in range(0, count_0):
            nums[i]=0
        for j in range(count_0, count_0+count_1):
            nums[j]=1
        for k in range(count_0+count_1, len(nums)):
            nums[k]=2
        
