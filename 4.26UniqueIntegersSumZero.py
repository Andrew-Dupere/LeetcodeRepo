"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""

class Solution(object):
    def sumZero(self, n):

        output = []

        if n == 1:
            output.append(0)
            return output
        
            
        for num in range(1,n):
            output.append(num)
            

        negativeArr = sum(output) * -1
        
        output.append(negativeArr)

        return output



        """
        :type n: int
        :rtype: List[int]
        """