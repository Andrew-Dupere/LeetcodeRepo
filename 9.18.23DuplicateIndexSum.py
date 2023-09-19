
"""

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 


"""





class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        #find a duplicate AND the diff of the 2 indeces must be <= k

        bigL = len(nums)

        if len(set(nums)) == bigL:
            return False

        for i in range(bigL):
            n = nums[i]
            if n in nums[i+1:] and abs(i - nums.index(n, i+1)) <= k:
                return True

        return False
               

        
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        