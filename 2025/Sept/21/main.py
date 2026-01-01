from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented_movie_to_shop: dict[int, list[tuple[int, int]]] = defaultdict(SortedList)
        self.rented_movies: list[tuple[int, int, int]] = SortedList()
        self.movie_shop_to_price: dict[tuple[int, int], int] = dict()
        for s, m, p in entries:
            self.movie_shop_to_price[(m, s)] = p
            self.unrented_movie_to_shop[m].add((p, s))

    def search(self, movie: int) -> List[int]:
        return [s for m, s in self.unrented_movie_to_shop[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        p: int = self.movie_shop_to_price[(movie, shop)]
        self.unrented_movie_to_shop[movie].remove((p, shop))
        self.rented_movies.add((p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p: int = self.movie_shop_to_price[(movie, shop)]
        self.rented_movies.remove((p, shop, movie))
        self.unrented_movie_to_shop[movie].add((p, shop))

    def report(self) -> List[List[int]]:
        return [[s, m] for p, s, m in self.rented_movies[:5]]