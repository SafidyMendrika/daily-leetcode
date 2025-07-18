from heapq import heapify, heappop, heappush


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 3
        
        def calculate_prefix_sums(values: list[int], n: int) -> list[int]:
            max_heap = [-v for v in values[:n]]
            heapify(max_heap)
            prefix_sums = [-sum(max_heap)]  
            
            for value in values[n:2*n]:
                current_sum = prefix_sums[-1]
                if -value > max_heap[0]:
                    current_sum -= -heappop(max_heap) 
                    heappush(max_heap, -value)        
                    current_sum += value                
                prefix_sums.append(current_sum)
            return prefix_sums
        
        prefix_sums = calculate_prefix_sums(nums, n)
        
        min_heap = [v for v in nums[2*n:]]
        heapify(min_heap)
        suffix_sums = [sum(min_heap)]  
        
        for value in nums[2*n-1:n-1:-1]:
            current_sum = suffix_sums[-1]
            if value > min_heap[0]:
                current_sum -= heappop(min_heap) 
                heappush(min_heap, value)          
                current_sum += value               
            suffix_sums.append(current_sum)
        
        suffix_sums = suffix_sums[::-1]  
        
        return min(p_sum - s_sum for p_sum, s_sum in zip(prefix_sums, suffix_sums))

solution = Solution()
nums = [7,9,5,8,1,3]
print(solution.minimumDifference(nums))