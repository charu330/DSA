# Maximum Sum of Distinct Subarrays With Length K

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        unique=set()
        new_sum=0
        sum=0
        maxsum=0
        while(j<len(nums)):
            if nums[j] in unique:
                sum=sum-nums[i]
                unique.remove(nums[i])
                i+=1
                continue 
            
            sum+=nums[j]
            unique.add(nums[j])
            if(j-i+1<k):
                j+=1
            elif(j-i+1==k):
                if(len(unique)==k):
                    new_sum=sum
                    maxsum=max(new_sum, maxsum)
                    sum=sum-nums[i]
                    unique.remove(nums[i])
                    i+=1
                    j+=1
                else:
                    new_sum=0
                    sum=sum-nums[i]
                    unique.remove(nums[i])
                    i+=1
                    j+=1
        return maxsum
