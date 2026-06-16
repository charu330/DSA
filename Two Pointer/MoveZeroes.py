class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        count=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[k]=nums[i]
                k+=1
                count+=1
 
        nums[k:]=[0]* (len(nums)-k)
        
