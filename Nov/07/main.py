from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]
        
        power = [0] * n
        for i in range(n):
            left = i - r
            if left < 0:
                left = 0
            right = i + r + 1
            if right > n:
                right = n
            power[i] = prefix[right] - prefix[left]
        
        def can(x: int) -> bool:
            add = [0] * (n + 1)
            curr = 0
            remain = k
            for i in range(n):
                curr += add[i]
                total = power[i] + curr
                if total < x:
                    need = x - total
                    remain -= need
                    if remain < 0:
                        return False
                    curr += need
                    end = i + 2 * r + 1
                    if end < n:
                        add[end] -= need
            return True

        low, high = min(power), max(power) + k
        ans = low
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
    

solution = Solution()
stations = [1,2,4,5,0]
r = 1
k = 2
print(solution.maxPower(stations,r,k))