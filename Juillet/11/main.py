import heapq
class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        free_rooms = list(range(n))
        heapq.heapify(free_rooms)

        busy = []
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                room = heapq.heappop(free_rooms)
                count[room] += 1
                heapq.heappush(busy, (end, room))
            else:
                free_time, room = heapq.heappop(busy)
                count[room] += 1
                heapq.heappush(busy, (free_time + duration, room))

        max_meetings = max(count)
        for i, c in enumerate(count):
            if c == max_meetings:
                return i
            

solution = Solution()
n = 3
meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
print(solution.mostBooked(n, meetings))