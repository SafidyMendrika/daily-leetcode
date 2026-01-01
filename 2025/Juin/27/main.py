from collections import defaultdict

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        
        n = len(s)

        indexes = defaultdict(list)

        for idx, char in enumerate(s):
            indexes[char].append(idx)
        
        for char in list(indexes.keys()):
            if len(indexes[char]) < k:
                indexes[char].clear()
                del indexes[char]
        
        chars_list = list(sorted(indexes.keys(), reverse=True))

        next_index = [[-1]*26 for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(26):
                next_index[i][j] = next_index[i+1][j]
            next_index[i][ord(s[i])-ord('a')] = i


        def occurs_k_times(cur_string):

            cnt = k
            last_idx = -1

            while cnt:

                for char in cur_string:
                    last_idx = next_index[last_idx+1][ord(char)-ord('a')]
                    if last_idx == -1:
                        return False
                
                cnt-=1
            
            return True



        def dfs(cur_sequence, last_idx, chars_list, length_largest):
            
            for x in chars_list:

                cur_idx = next_index[last_idx+1][ord(x)-ord('a')]

                if cur_idx == -1:
                    continue

                new_sequence = cur_sequence + x

                if occurs_k_times(new_sequence):
                    if len(new_sequence) not in length_largest:
                        length_largest[len(new_sequence)] = new_sequence

                    dfs(new_sequence, cur_idx, chars_list, length_largest)
        
        length_largest = {0: ""}
        dfs("", -1, chars_list, length_largest)
        
        return length_largest[max(length_largest.keys())]

solution = Solution()
s = "bb"
k = 2


print(solution.longestSubsequenceRepeatedK(s,k))