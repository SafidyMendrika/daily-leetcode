from sortedcontainers import SortedList
import collections

class Solution:
  def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
    ans = []
    windowSum = 0
    count = collections.Counter()
    top = SortedList()  
    bot = SortedList() 

    def update(num: int, freq: int) -> None:
      nonlocal windowSum
      if count[num] > 0:  
        if [count[num], num] in bot:
          bot.remove([count[num], num])
        else:
          top.remove([count[num], num])
          windowSum -= num * count[num]
      count[num] += freq
      if count[num] > 0:
        bot.add([count[num], num])

    for i, num in enumerate(nums):
      update(num, 1)
      if i >= k:
        update(nums[i - k], -1)
      while bot and len(top) < x:
        countB, b = bot.pop()
        top.add([countB, b])
        windowSum += b * countB
      while bot and bot[-1] > top[0]:
        countB, b = bot.pop()
        countT, t = top.pop(0)
        bot.add([countT, t])
        top.add([countB, b])
        windowSum += b * countB
        windowSum -= t * countT
      if i >= k - 1:
        ans.append(windowSum)

    return ans

solution = Solution()  
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
print(solution.findXSum(nums,k,x))