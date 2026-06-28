# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        maxlen=0
        count=0
        if(k>=len(nums)):
            return len(nums)
        while(j<len(nums)):
            if(nums[j]==0):
                count+=1
            if(count<=k):
                maxl=j-i+1
                maxlen=max(maxl, maxlen)
                j+=1
            elif(count>k):
                if(nums[i]==0):
                    count-=1
                i+=1
                j+=1
        return maxlen    

        
