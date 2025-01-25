class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        indexed_nums = sorted([(num, i) for i, num in enumerate(nums)])
        
        groups = []
        current_group = [indexed_nums[0]]
        
        for i in range(1, len(indexed_nums)):
            if indexed_nums[i][0] - indexed_nums[i-1][0] <= limit:
                current_group.append(indexed_nums[i])
            else:
                groups.append(current_group)
                current_group = [indexed_nums[i]]
        
        groups.append(current_group)
        
        result = [0] * len(nums)
        
        for group in groups:
            sorted_group = sorted(group, key=lambda x: x[0])
            sorted_indices = sorted(group, key=lambda x: x[1])
            for (val, _), (_, orig_idx) in zip(sorted_group, sorted_indices):
                result[orig_idx] = val
        
        return result
    
if __name__ == "__main__":
    nums = [5,100,44,45,16,30,14,65,83,64]
    limit = 2
    s = Solution()
    print(s.lexicographicallySmallestArray(nums, limit))