# Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        min_len= float('inf')
        sum=0
        while(j<len(nums)):
            sum=sum+nums[j]
            if(sum<target):
                j+=1
            elif(sum==target):
                min_length= j-i+1
                min_len=min(min_len, min_length)
                j+=1
            elif(sum>target):
                while(sum>=target):
                    min_length = j-i+1          
                    min_len = min(min_len, min_length)
                    sum=sum-nums[i]
                    i+=1
                j+=1
        if(min_len != float('inf')):
            return min_len
        else:
            return 0     


        
