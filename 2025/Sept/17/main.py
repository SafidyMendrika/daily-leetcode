from typing import List
from heapq import heappush,heappop,heapify
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_rating = {}
        self.dic = {} 
        for i in range(len(foods)):
            self.food_to_cuisine[foods[i]] = cuisines[i]
            self.food_rating[foods[i]] = ratings[i]
            if cuisines[i] in self.dic:
                heappush(self.dic[cuisines[i]], (-ratings[i], foods[i])) 
            else:
                tmp =[(-ratings[i], foods[i])]
                heapify(tmp)
                self.dic[cuisines[i]] = tmp
    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating
        heappush(self.dic[self.food_to_cuisine[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        neg_rating, name = self.dic[cuisine][0]
        while neg_rating != -self.food_rating[name]:
            heappop(self.dic[cuisine])
            neg_rating, name = self.dic[cuisine][0]
        return name