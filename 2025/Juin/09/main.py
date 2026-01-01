class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        decrement_amount = 1
        base = 1
        while n // base >= 10:
            decrement_amount = decrement_amount * 10 + 1
            base *= 10

        cur = 1
        while k > 1:
            decrease_distance = False
            furthest = max(1, min((k - 1) // decrement_amount, n // base - cur))
            potential_next_cur = cur + furthest
            potential_next_k = k - decrement_amount * furthest
            if potential_next_cur > n // base:
                potential_next_k += base - (n + 1) % base
                decrease_distance = True
            
            if potential_next_k < 1:
                k -= 1
                cur *= 10
                decrease_distance = True
            else:
                cur = potential_next_cur
                k = potential_next_k
            if decrease_distance:
                base //= 10
                decrement_amount //= 10
        return cur


solution = Solution()
n = 13
k = 2

print(solution.findKthNumber(n,k))  