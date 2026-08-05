# 2149. Rearrange Array Elements by Sign

# with 2 pass and extra space

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        res=[]
        i=0
        for i in range(len(nums)):
            if(nums[i]>=0):
                pos.append(nums[i])
            elif(nums[i]<0):
                neg.append(nums[i])
        j=0
        while(j<len(pos)):
            res.append(pos[j])
            res.append(neg[j])
            j+=1
        return res
        
