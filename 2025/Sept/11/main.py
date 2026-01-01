class Solution:
   def sortVowels(self, s: str) -> str:
        t = ""
        arr = []
        result = []
        set = {'a','e','i','o','u','A','E','I','O','U'}
        for ch in s :
            if ch in set :
                arr.append(ch)

        arr.sort() 
        i =0
        for ch in s :
            if ch in set :
                result.append(arr[i])
                i += 1
            else:
                result.append(ch)
        return "".join(result)
        

solution = Solution()
s = "lEetcOde"
print(solution.sortVowels(s))