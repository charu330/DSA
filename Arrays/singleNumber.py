# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp={}
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        for i, j in mp.items():
            if(j==1):
                return i
            

        
