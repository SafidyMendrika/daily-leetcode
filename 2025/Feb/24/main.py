class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        bob_time = [-1] * n
        
        def bob_dfs(node, parent, time):
            if node == 0:
                bob_time[node] = time
                return True
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    if bob_dfs(neighbor, node, time + 1):
                        bob_time[node] = time
                        return True
            
            return False
        
        bob_dfs(bob, -1, 0)
        
        def alice_dfs(node, parent, time, income):
            curr_income = income
            
            if time < bob_time[node] or bob_time[node] == -1:
                curr_income += amount[node]
            elif time == bob_time[node]:
                curr_income += amount[node] // 2
            
            is_leaf = True
            max_child_income = float('-inf')
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    is_leaf = False
                    child_income = alice_dfs(neighbor, node, time + 1, curr_income)
                    max_child_income = max(max_child_income, child_income)
            
            if is_leaf:
                return curr_income
            
            return max_child_income
        
        return alice_dfs(0, -1, 0, 0)
    

edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]

s = Solution()

print(s.mostProfitablePath(edges,bob,amount))