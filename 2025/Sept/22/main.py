from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        maxl = 0
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
            maxl = max(maxl, dic[num])
        
        res = 0
        for value in dic.values():
            if value == maxl:
                res += value
        return res