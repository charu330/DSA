class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        l=0
        r=len(nums)-1
        count=0
        while (l<r):
            if(nums[l]!=0):
                l+=1
            elif(nums[l]==0 and nums[r]!=0):
                l+=1
                r-=1
                count+=1
            elif(nums[l]==0 and nums[r]==0):
                r-=1
            else:
                return 0
        return count



        