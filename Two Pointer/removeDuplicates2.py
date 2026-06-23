# Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        count=1
        k=2

        if len(nums)<=2:
            return len(nums)


        
        for i in range(2, len(nums)):
            if(nums[i]!= nums[k-2]):
                nums[k]=nums[i]
                k+=1
            
        return k
