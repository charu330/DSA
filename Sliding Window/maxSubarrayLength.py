#  Length of Longest Subarray With at Most K Frequency

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        maxlen=0
        mp=dict()
        while(j<len(nums)):
            if nums[j] not in mp:
                mp[nums[j]]=1
            else:
                mp[nums[j]]+=1
            if(mp[nums[j]]<=k):
                maxl=j-i+1
                maxlen=max(maxlen, maxl)
                j+=1
            elif(mp[nums[j]]>k):
                while(mp[nums[j]]>k):
                    mp[nums[i]]-=1
                    i+=1
                j+=1
        return maxlen
        
