# Leetcode problem Dec 21
# Problem description:
# https://leetcode.com/problems/word-break

# A second version that passes the submission test cases,
# but still a bit slow.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        length = len(s)
        memo = [None]*(length+1)
        #memo[0] = True


        def creatable(sub: str, start_indx: int) -> bool:
            print(f"str: {sub} start_indx: {start_indx}")
 
            if memo[start_indx] is not None:
                return memo[start_indx]

            if len(sub)==0:
                return True
        

            for w in wordDict:
                suffix_indx = start_indx + len(w)
                if sub.startswith(w) and creatable(sub[len(w):], suffix_indx):
                    memo[start_indx] = True
                    return True
            
            memo[start_indx]=False
            return False


        ans = creatable(s, 0)

        return memo[0]
