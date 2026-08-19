# 33. Search in Rotated Sorted Array


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if(nums[mid]==target):
                ans=mid
            if nums[low]<=nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            elif nums[low] > nums[mid]:
                if target <= nums[high] and target > nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
        return ans



        
