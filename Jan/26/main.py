from collections import defaultdict

class Solution:
    def count_size_two_extra(self):
        visited = [False] * self.n
        res = 0

        for a, b in self.pairs:
            self.max[a] = 0
            self.max[b] = 0

            visited[a] = True
            self.dfs(b, visited, 0, b)
            visited[a] = False

            visited[b] = True
            self.dfs(a, visited, 0, a)
            visited[b] = False

            if self.max[a] > 0 and self.max[b] > 0:
                res += (self.max[a] + self.max[b])
            else:
                res += max(self.max[a], self.max[b])
            res += 2
        return res

    def dfs(self, cur, visited, length, start):
        if visited[cur]:
            return
        self.max[start] = max(self.max.get(start, 0), length)
        visited[cur] = True
        for neighbor in self.graph.get(cur, []):
            if not visited[neighbor]:
                self.dfs(neighbor, visited, length + 1, start)
        visited[cur] = False

    def count_cycle(self):
        visited = [False] * self.n
        rec_stack = [False] * self.n

        for i in range(self.n):
            self.is_cyclic_util(i, visited, rec_stack, 0)

    def is_cyclic_util(self, i, visited, rec_stack, count):
        if rec_stack[i]:
            self.single_max_cycle_size = max(self.single_max_cycle_size, count)
            if count == 2:
                self.pairs.append((i, self.favorite[i]))
            return
        if visited[i]:
            return
        visited[i] = True
        rec_stack[i] = True
        for child in self.graph.get(i, []):
            self.is_cyclic_util(child, visited, rec_stack, count + 1)
        rec_stack[i] = False

    def maximumInvitations(self,favorite):
        self.favorite = favorite
        self.n = len(favorite)
        self.graph = defaultdict(list)
        self.pairs = []
        self.single_max_cycle_size = 0
        self.max = {}

        for i, f in enumerate(favorite):
            self.graph[f].append(i)

        self.count_cycle()
        size_two_extra = self.count_size_two_extra()
        return max(self.single_max_cycle_size, size_two_extra)

if __name__ == "__main__":
    arr = [2,2,1,2]
    s = Solution()
    print(s.maximumInvitations(arr))