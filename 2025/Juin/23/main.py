class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def to_base_k(num: int, base: int) -> str:
            res = []
            while num > 0:
                res.append(str(num % base))
                num //= base
            return ''.join(reversed(res)) if res else "0"

        def generate_palindromes():
            length = 1
            while True:
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[-2::-1])
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[::-1])
                length += 1

        gen = generate_palindromes()
        count = 0
        total = 0

        while count < n:
            num = next(gen)
            if is_palindrome(to_base_k(num, k)):
                total += num
                count += 1
        return total

solution = Solution()
k = 2
n = 5

print(solution.kMirror(k,n))