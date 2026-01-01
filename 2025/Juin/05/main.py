class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))  

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        result = []
        for c in baseStr:
            smallest = chr(find(ord(c) - ord('a')) + ord('a'))
            result.append(smallest)

        return ''.join(result)


solution = Solution()
s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"

print(solution.smallestEquivalentString(s1, s2, baseStr))  