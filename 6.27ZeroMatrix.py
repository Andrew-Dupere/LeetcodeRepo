""""
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""

#change all values in the list item to zero
#save the index of the zero to a variable and change all other values at that index to zero

import copy

class Solution(object):

    def setZeroes(self, matrix):

        neo = copy.deepcopy(matrix)            

        for row in neo:

            rowidx = neo.index(row)
            
            
            if 0 in row:

                for idx in range(len(row)):

                    matrix[rowidx][idx] = 0

            for num in range(len(row)):
                if row[num] == 0:
                    for idx in range(len(matrix)):
                        matrix[idx][num] = 0

                   
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print(matrix)

x = Solution()
x.setZeroes(matrix)

print(matrix)