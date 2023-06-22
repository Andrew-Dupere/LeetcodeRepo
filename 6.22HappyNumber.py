"""

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

"""


"""
Testing numbers from 0 to 100000, it seems the most a number can run through the recursive function
is its number of digits + 2 (so a 4 digit number can run through a max of 6 times before it can be considered an unhappy number)

"""

class Solution(object):
    def isHappy(self, n):

        n2 = sum(int(num)**2 for num in str(n))

        counter = 0
        while n2 != 1:
            if counter < (len(str(n))+3):
                n2 = sum(int(num)**2 for num in str(n2))
                counter +=1
            else:
                return False            

        else:
            return True
           
        """
        :type n: int
        :rtype: bool
        """

x = Solution()
print(x.isHappy(7))
