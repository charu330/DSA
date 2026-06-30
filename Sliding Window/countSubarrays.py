#Count Subarrays Where Max Element Appears at Least K Times

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        count=0
        maxel=nums[0]
        rescount=0
        for i in range(len(nums)):
            maxel= max(maxel, nums[i])
           
        i=0
        while(j<len(nums)):
            if(nums[j]==maxel):
                count+=1
            if(count<k):
                pass
            elif(count>=k):
                while(count>=k):
                    if(nums[i]==maxel):
                        count-=1
                    i+=1
            
            rescount+=i
            j+=1
        return rescount
                    
        
