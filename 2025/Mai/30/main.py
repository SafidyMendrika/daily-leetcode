class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        def get_distances(start):
            n = len(edges)
            dist = [-1] * n
            d = 0
            while start != -1 and dist[start] == -1:
                dist[start] = d
                start = edges[start]
                d += 1
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        min_dist = float('inf')
        result = -1
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist or (max_dist == min_dist and i < result):
                    min_dist = max_dist
                    result = i
        return result


solution = Solution()

edges = [2,2,3,-1]
node1 = 0
node2 = 1

print(solution.closestMeetingNode(edges, node1, node2))  