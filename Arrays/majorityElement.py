# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp={}
        i=0
        res=0
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]]=1
            else:
                mp[nums[i]]+=1
        for i, j in mp.items():
            if j> len(nums)//2:
                res= i
        return res
