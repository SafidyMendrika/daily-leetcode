from typing import List
import heapq
class Solution:
    def findXSum(self, nums : List[int], k : int, x : int):
        n = len(nums)
        res = []
        for i in range(0, n-k+1):
            newNums = nums[i: i+k]
            mapp = {}
            for num in newNums:
                mapp[num] = mapp.get(num, 0) + 1
            minHeap = []
            for val, freq in mapp.items():
                item = (freq, val)
                if len(minHeap) < x:
                    heapq.heappush(minHeap, item)
                else:
                    heapq.heappushpop(minHeap, item)
            summ = 0
            for freq, val in minHeap:
                summ += freq * val
            res.append(summ)
        return res
    
solution = Solution()
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
print(solution.findXSum(nums,k,x))