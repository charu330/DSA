# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low1=0
        high1=len(nums)-1
        first=-1
        last=-1
        while (low1<=high1):
            mid=(low1+high1)//2
            if nums[mid]==target:
                last=mid
                low1=mid+1
            elif nums[mid]<target:
                low1=mid+1
            else:
                high1=mid-1
        low2=0
        high2=len(nums)-1
        while (low2<=high2):
            mid=(low2+high2)//2
            if nums[mid]==target:
                first=mid
                high2=mid-1
            elif nums[mid]<target:
                low2=mid+1
            else:
                high2=mid-1 
        return [first, last]
