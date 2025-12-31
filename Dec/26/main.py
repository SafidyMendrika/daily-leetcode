class Solution:
    def bestClosingTime(self, customers: str) -> int:
        maxi = 0
        profit = 0
        index = 0

        for i, x in enumerate(customers):
            if x == 'Y':
                profit += 1
            else:
                profit -= 1

            if profit > maxi:
                maxi = profit
                index = i

        if maxi == 0:
            return 0
        return index + 1