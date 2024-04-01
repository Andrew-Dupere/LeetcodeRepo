"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

"""

class Solution(object):
    def longestCommonPrefix(self, strs):

        
        #if there is only one word in the list strs then return the word
        if len(strs) == 1:
            return strs[0]

        #use strs[0] as a check against strs[1:] 
        check = strs[0]

        output = ''
        #iterate through each word at index i, if the letter at each index is the same then
        for i in range(len(check)):

            e = True

            try:
                for word in strs[1:]:                 
                                               

                    if word[i] != check[i]:
                        e = False

                if e:

                    output += word[i]
                
                if not e:

                    return output

            except:
                continue
                     

        return output
    

r = Solution()
print(r.longestCommonPrefix(["flower","flow","flight"]))

