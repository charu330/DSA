# Limit Occurrences in Sorted Array. Return an array such that each distinct element appears at most k times, while preserving the relative order of the elements in nums.

# Note: If a distinct element appears at least k times, then it must appear exactly k times in the resulting array.

class Solution {
    public int[] limitOccurrences(int[] nums, int k) {
         Map<Integer, Integer> new_arr = new HashMap<>();
         count=1
         for(int i=0;i<nums.length;i++)
         {
            int j=i+1;
            new_arr.put(nums[i], count);
            if(nums[i]==nums[j])
            {
                count++;
            }
            new_arr.put(nums[i], count);
            
         }
        
    }
}
