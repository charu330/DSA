# Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=0
        avg=0
        max_avg=float('-inf')
        sum=0
        while(j<len(nums)):
            sum=sum+nums[j]
            if((j-i+1) < k):
                j+=1
            elif((j-i+1)==k):
                avg=sum/k
                max_avg= max(max_avg, avg)
                sum=sum-nums[i]
                j+=1
                i+=1
        return max_avg

        
