# Leetcode problem Day 14
# Problem description:
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# This version does not work at all - getting weird error in index to digits string being out of range.
# Somehow in the Leetcode environment, the statements above the while loop are run within the while
# loop, decrementing the index.
# The next version should use backtracking and recursion.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        d2c_map = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz" }

        indx = len(digits) - 1
        print(f"Length of digits string: {len(digits)}")
        print(f"Value of indx: {indx}")
        print(f"The digits string: {digits}")

        length = len( d2c_map[ digits[indx] ] )
        working_list = ["" for i in range(length) ]
        
        while indx >= 0:
            left_generator = d2c_map[ digits[indx] ]
            new_elts = []
            for c in left_generator:
                new_sublist = [ c+elt for elt in working_list ]
                new_elts.extend(new_sublist)
            working_list.extend(new_elts)
            indx-=1
        
        return working_list

