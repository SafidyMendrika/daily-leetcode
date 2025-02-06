from collections import defaultdict

class Solution(object):
        
    def tupleSameProduct(self,nums):
        product_pairs = defaultdict(int)
        n = len(nums)   
        
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_pairs[product] += 1

        count = 0
        for product, freq in product_pairs.items():
            if freq > 1:
                count += (freq * (freq - 1) // 2) * 8  
        
        return count

if __name__ == "__main__":
    nums = [1,2,4,5,10]
    s = Solution()
    print(s.tupleSameProduct(nums))