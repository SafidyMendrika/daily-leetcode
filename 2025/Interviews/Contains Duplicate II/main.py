class Solution : 
    def containsNearbyDuplicate(self,nums, k):
        index_map = {}  

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True  
            index_map[num] = i 

        return False  

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,1]
    k = 3
    print(s.containsNearbyDuplicate(nums,k))
    