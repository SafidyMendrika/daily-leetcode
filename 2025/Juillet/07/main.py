import heapq
class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda x:x[0])
        heap_list = []
        event_attended = 0
        max_day = max([i[1] for i in events])
        min_day = min([i[0] for i in events])
        length = len(events)
        j=0
        print(max_day,min_day)
        for i in range(min_day,max_day+1):
            
            while j<length and events[j][0]<=i:
                end_tmp = events[j][1]
                heapq.heappush(heap_list,end_tmp)
                j+=1
                

            while heap_list and heap_list[0]<i:
                    heapq.heappop(heap_list)

            if heap_list:
                heapq.heappop(heap_list)
                event_attended+=1
        return event_attended
    
solution = Solution()
events= [[1,2],[2,3],[3,4],[1,2]]

print(solution.maxEvents(events))  