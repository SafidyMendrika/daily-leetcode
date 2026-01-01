class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringified = str(x)
        return stringified[::-1] == stringified