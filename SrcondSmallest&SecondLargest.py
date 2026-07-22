class Solution:
    def secondLargestElement(self, nums):
        n=len(nums)
        if n==0 or n==1:
            return -1
        maxx=float('-inf')
        minn=float('inf')
        for i in range (n):
            if nums[i]>maxx:
                maxx=nums[i]
            if nums[i]<minn:
                minn=nums[i]
        secondLargest=float('-inf')
        secondSmallest=float('inf')
        for i in range(n):
            if nums[i]>secondLargest and nums[i]!=maxx:
                secondLargest=nums[i]
            if nums[i]<secondSmallest and nums[i]!=minn:
                secondSmallest=nums[i]
        return secondLargest,secondSmallest