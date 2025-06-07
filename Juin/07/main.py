from collections import defaultdict
from string import ascii_lowercase

class Solution:
    def clearStars(self, s: str) -> str:
        char_indices = defaultdict(list)
        n = len(s)  
        remove = [False] * n  
      
        for i, char in enumerate(s):
            if char == "*":
                remove[i] = True
                for alphabet in ascii_lowercase:
                    if char_indices[alphabet]:
                        remove[char_indices[alphabet].pop()] = True
                        break
            else:
                char_indices[char].append(i)
      
        return "".join(char for i, char in enumerate(s) if not remove[i])


solution = Solution()
s = "aaba*"

print(solution.clearStars(s))  