from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def help_me_god(s):
            vow = {'a','e','i','o','u'}
            if s[0] in vow and s[-1] in vow:
                return 1
            else:
                return 0

        prefix = [0]*(len(words)+1)
        prefix[0] = help_me_god(words[0])
        for i in range(len(words)):
            prefix[i+1] = prefix[i] + help_me_god(words[i])

        res = []
        for l,r in queries:
            res.append(prefix[r+1]-prefix[l])
        return res

solution = Solution()
words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
print(solution.vowelStrings(words, queries))