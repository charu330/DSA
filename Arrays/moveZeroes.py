# 283. Move Zeroes


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        index=-1
        for i in range(len(nums)):
            if(nums[i]==0):
                index=i
                break
        if index==-1:
            return None
        j=index
        k=j+1
        while(k< len(nums)):
            if(nums[j]==0):
                if(nums[k]!=0):
                    nums[j],nums[k]=nums[k],nums[j]
                    j+=1
                    k+=1
                elif(nums[k]==0):
                    k+=1
