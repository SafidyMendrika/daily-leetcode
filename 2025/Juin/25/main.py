class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1_last_neg_index = bisect_left(nums1,0)-1
        nums2_last_neg_index= bisect_left(nums2,0)-1
        num1_neg =[] if nums1_last_neg_index<0 else nums1[:nums1_last_neg_index+1]
        num1_pos =[] if nums1_last_neg_index == len(nums1)-1 else nums1[nums1_last_neg_index+1:]
        num2_neg =[] if nums2_last_neg_index < 0 else nums2[:nums2_last_neg_index+1]
        num2_pos =[] if nums2_last_neg_index == len(nums2)-1 else nums2[nums2_last_neg_index+1:]
        neg_product_count = len(num1_neg)* len(num2_pos) + len(num2_neg)* len(num1_pos)
        if_k_in_negative = neg_product_count>= k
        min_possible_val = -10**10
        max_possible_val =10**10+1

        def solve(arr1,arr2,product):
            l1 = len(arr1)-1
            l2 = len(arr2)-1
            temp = 0
            for num1 in arr1:
                while l2>=0:
                    if num1 * arr2[l2]<=product:
                        temp += l2+1
                        if temp>= k:
                            return temp
                        break
                    l2-=1
            return temp
        result = 10**10+2
        if if_k_in_negative:

            num1_pos.reverse()
            num2_pos.reverse()
            max_possible_val =-1
            while min_possible_val <= max_possible_val:
                mid = (min_possible_val + max_possible_val)//2
                temp = solve(num2_neg,num1_pos,mid)+solve(num1_neg,num2_pos,mid)
                if temp >=k:
                    result = min(result,mid)
                    max_possible_val = mid-1
                else:
                    min_possible_val = mid+1
        else:
            min_possible_val =0
            k = k-neg_product_count
            num1_neg.reverse()
            num2_neg.reverse()
            while min_possible_val <= max_possible_val:
                mid = (min_possible_val + max_possible_val)//2
                temp = solve(num1_pos,num2_pos,mid)+solve(num1_neg,num2_neg,mid)
                if temp >=k:
                    result = min(result,mid)
                    max_possible_val = mid-1
                else:
                    min_possible_val = mid+1


       
        return result if result !=10**10+2  else 0
    

solution = Solution()
nums1 = [-2,-1,0,1,2]
nums2 = [-3,-1,2,4,5]
k = 3

print(solution.kthSmallestProduct(nums1,nums2,k))