import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        h = []
        for p, t in classes:
            delta = (p+1)/(t+1) - p/t
            heapq.heappush(h, (-delta, p, t))
        for _ in range(extraStudents):
            d, p, t = heapq.heappop(h)
            p += 1
            t += 1
            delta = (p+1)/(t+1) - p/t
            heapq.heappush(h, (-delta, p, t))
        return sum(p/t for _, p, t in h) / len(classes)

solution = Solution()
classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
print(solution.maxAverageRatio(classes, extraStudents))