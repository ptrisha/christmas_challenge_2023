# Leetcode problem Dec 21
# Problem description:
# https://leetcode.com/problems/word-break

# A preliminary version that does not work.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        length = len(s)
        memo = [None]*(length+1)
        memo[0] = True

        word_lengths = [len(s) for s in wordDict]
        max_wordlen = max(word_lengths)
        min_wordlen = min(word_lengths)
        print(f"Min word len: {min_wordlen}")
        print(f"Max word len: {max_wordlen}")

        for i in range(1, min_wordlen):
            memo[i] = False

        def creatable(sub: str) -> bool:
            print(f"str: {sub} ")
            s_len = len(sub)
            if memo[s_len] is not None:
                return memo[s_len]
        
            if s_len == 0:
                return True

            if s_len < min_wordlen:
               return False

            if sub in wordDict:
                return True

            for i in range(min_wordlen, max_wordlen+1):
                print(f"pre: {sub[:i]} post: {sub[i:]} i: {i}")
                if creatable(sub[:i]):
                    if creatable(sub[i:]):
                        memo[s_len] = True
                        return True

            memo[s_len] = False
            return False

        ans = creatable(s)

        return ans
    
    