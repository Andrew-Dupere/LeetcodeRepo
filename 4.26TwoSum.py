class Solution(object):


    def twoSum(self, nums, target):
        res = []


        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    res.extend([i,j])
        return res[:2]

sol = Solution()

print(sol.twoSum([2,7,11,15],9))


