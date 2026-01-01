class Solution(object):
    def findWordsContaining(self, words,x):
        return [i for i in range(len(words)) if x in words[i]]



solution = Solution()

words1 = ["leet", "code"]
x = "e"
result = solution.findWordsContaining(words1, x)
print(result)