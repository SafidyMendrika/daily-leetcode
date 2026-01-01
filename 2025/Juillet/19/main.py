class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        res = []
        for f in folder:
            if not res:
                res.append(f)
            else:
                prev = res[-1]
                if f.startswith(prev) and len(f) > len(prev) and f[len(prev)] == '/':
                    continue
                else:
                    res.append(f)
        return res

solution = Solution()
folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
print(solution.removeSubfolders(folder))