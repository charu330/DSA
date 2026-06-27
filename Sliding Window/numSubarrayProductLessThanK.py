# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        result=0
        product=1
        if(k<=1):
            return 0
        while(j<len(nums)):
            product= product * nums[j]
            if(product<k):
                result+=(j-i+1)
                j+=1
            elif(product>=k):
                product= product//nums[i]
                i+=1
                if(i>j):
                    product=1
                    j+=1
                else:
                    product = product // nums[j]
            
        return result
        
