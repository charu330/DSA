# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        ans=n
        while low<=high:
            mid=(low+high)//2
            
            if target > nums[mid]:
                low=mid+1
            elif target <= nums[mid]:
                ans= mid
                high=mid-1
        return ans
    

        
