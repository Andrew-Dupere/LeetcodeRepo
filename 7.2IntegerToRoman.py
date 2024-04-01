"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.



probably need to use % operator 

divide the input evenly into the values for each symbol using the % operator

then create conditional statements for values that have multiple solutions


"""



class Solution(object):
        
    #     Symbol       Value
    # I             1    num % 1
    # V             5    num % 5
    # X             10    num % 10
    # L             50    num % 50
    # C             100    num % 100    
    # D             500    num % 500    
    # M             1000   num % 1000



    def intToRoman(self, num): #this function can be a series of if statements to check the size of the input followed by a series of conditionals to create the roman

        if num < 5: 
             roman += 'I'*num

        #right here I'm thinking of taking the number and subtracting its value as I append the corresponding roman to the output
        #so if 9 is the input, I'll subtract 5 from 9 and add a V, then I'll subtract 1 and add an I until the input number is zero

        roman = ''    
        
        
        return roman

    def R2(self, num): #this function will reduce the number and add characters to the output until the number is zero
        
        while num > 0:
             if num > 1:
                 pass

            
    def R3(self, num): #this function will contain a dictionary with the value of each numeral key being the correct output for a given input

        roman = ''

        Legion = {
             'I': [num / 1],             
             'V': [num / 5],             
             'X': [num / 10],             
             'L': [num / 50],             
             'C': [num / 100],             
             'D': [num / 500],             
             'M': [num / 1000],             
        }

        for key, val in Legion.items():
             if val[0] >= 1:
                while num > val[0]:
                     num - val[0]
                     roman += key
        return roman
                     
                  
                  
    
                  
             


    



        """
        :type num: int
        :rtype: str
        """

