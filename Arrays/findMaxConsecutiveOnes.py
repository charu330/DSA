485. Max Consecutive Ones


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        index=-1
        count=0
        maxi=0
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if nums[i]==1:
               count+=1
               maxi=max(maxi, count)
            else:
                count=0
        return maxi


            
            
        
