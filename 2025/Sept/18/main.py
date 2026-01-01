import heapq
from typing import List
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasksHeap = []
        self.tasksHashMap = {}

        for task in tasks:
            self.tasksHashMap[task[1]] = task
            heapq.heappush(self.tasksHeap, (-task[2], -task[1]))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasksHashMap[taskId] = [userId, taskId, priority]
        heapq.heappush(self.tasksHeap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        task = self.tasksHashMap.get(taskId)
        self.tasksHashMap[taskId] = [task[0], task[1], newPriority]
        heapq.heappush(self.tasksHeap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.tasksHashMap[taskId]
    def execTop(self) -> int:
        if not self.tasksHashMap or not self.tasksHeap:
            return -1
        highiest = heapq.heappop(self.tasksHeap)
        while -highiest[1] not in self.tasksHashMap or -highiest[0] != self.tasksHashMap[-highiest[1]][2]:
            if not self.tasksHeap:
                return -1
            highiest = heapq.heappop(self.tasksHeap)
        userId = self.tasksHashMap[-highiest[1]][0]
        del self.tasksHashMap[-highiest[1]]
        return userId