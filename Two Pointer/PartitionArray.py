# Partition Array According to Given Pivot
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list_l=[]
        list_r=[]
        list_p=[]
     
        for i in range(len(nums)):
            if(nums[i]<pivot):
                list_l.append(nums[i])
            elif(nums[i]>pivot):
                list_r.append(nums[i])
            else:
                list_p.append(nums[i])
        joined_array = list_l + list_p+ list_r
        return joined_array
