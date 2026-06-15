# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i=0
        j=i+1
        ui=1
        count=len(nums)
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return 1
        while(i<j and j< len(nums)):
            if (nums[i]==nums[j]):        
                j=j+1
                count= count-1
                
            else:
                nums[ui]=nums[j]
                ui=ui+1
                i=j
                j=j+1
        return count

        
