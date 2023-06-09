"""

https://leetcode.com/problems/add-digits/

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

"""

class Solution(object):
    def addDigits(self, num):

        
        while num > 9:
            numsList = [int(num) for num in str(num)]
            num = sum(numsList)
            self.addDigits(num)
        else:
            return num
        
    
        """
        :type num: int
        :rtype: int
        """
x = Solution()
print(x.addDigits(38))

