"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4

Input: nums = [2,7,9,3,1]
Output: 12


"""

class Solution(object):
    def rob(self, nums):

        p1 = 0
        p2 = 0
        
        for n in nums:
            temp = max(n + p1, p2)
            p1 = p2
            p2 = temp        

        return p2

sol = Solution()
    
sol.rob([2,7,9,3,1])

sol.rob([1,2,3,1])

sol.rob([2,1,1,2]) 


