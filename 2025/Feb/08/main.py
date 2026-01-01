class NumberContainers:
    def __init__(self):
        self.index_to_num = {}  
        self.num_to_indices = {}  
        from heapq import heappush, heappop
        self.heappush = heappush
        self.heappop = heappop
        
    def change(self, index, number):
        if index in self.index_to_num:
            old_num = self.index_to_num[index]
            while self.num_to_indices[old_num] and self.num_to_indices[old_num][0] == index:
                self.heappop(self.num_to_indices[old_num])
                
        self.index_to_num[index] = number
        
        if number not in self.num_to_indices:
            self.num_to_indices[number] = []
        self.heappush(self.num_to_indices[number], index)
        
    def find(self, number):
        if number in self.num_to_indices and self.num_to_indices[number]:
            while (self.num_to_indices[number] and 
                  self.index_to_num.get(self.num_to_indices[number][0]) != number):
                self.heappop(self.num_to_indices[number])
                
            if self.num_to_indices[number]:
                return self.num_to_indices[number][0]
        
        return -1
    
