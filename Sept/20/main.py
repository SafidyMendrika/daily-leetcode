from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  
        self.packet_set = set()  
        self.dest_map = defaultdict(list)  

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        
        if packet in self.packet_set:
            return False
        
        if len(self.queue) == self.memoryLimit:
            old_src, old_dst, old_time = self.queue.popleft()
            self.packet_set.remove((old_src, old_dst, old_time))
            idx = bisect.bisect_left(self.dest_map[old_dst], old_time)
            if idx < len(self.dest_map[old_dst]) and self.dest_map[old_dst][idx] == old_time:
                self.dest_map[old_dst].pop(idx)
        
        self.queue.append(packet)
        self.packet_set.add(packet)
        self.dest_map[destination].append(timestamp) 
        return True

    def forwardPacket(self):
        if not self.queue:
            return []
        
        src, dst, time = self.queue.popleft()
        self.packet_set.remove((src, dst, time))
        
        idx = bisect.bisect_left(self.dest_map[dst], time)
        if idx < len(self.dest_map[dst]) and self.dest_map[dst][idx] == time:
            self.dest_map[dst].pop(idx)
        
        return [src, dst, time]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_map[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        return right - left
