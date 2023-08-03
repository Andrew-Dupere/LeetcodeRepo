"""

https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]


"""

#each number in the triangle is the sum of the two numbers directly above it

#given num rows return the "first num rows" 

#return a list containing a list of each row

#each number is the sum of the two numbers directly above it

#given num rows return the "first num rows" 

#return a list containing a list of each row

class Solution(object):
    def generate(self, numRows):
        output = [[1]]        

        if numRows == 1:
            return [[1]]            

        
        if numRows > 1:
            for num in range(1,numRows):
                prev = output[-1]
                currentRow = [1]

                for i in range(1,num):
                    currentRow.append(prev[i-1]+ prev[i])


                currentRow.append(1)
                output.append(currentRow)

        return output

        """
        :type numRows: int
        :rtype: List[List[int]]
        """
