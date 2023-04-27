"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

class Solution(object):
    def reverse(self, x):

        

        try:

            if x > 0:
                result = int(str(x)[::-1])
            else:
                result = int((str(x)[1::])[::-1]) * -1

        except:
            return 0  
        
        if result > -2**31 and result < 2**31 - 1:

            return result

        return 0


        """
        :type x: int
        :rtype: int
        """