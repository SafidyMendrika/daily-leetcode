class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()

        trainers.sort()

        i = j = 0
        count = 0

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count
            

solution = Solution()
players = [4,7,9]
trainers = [8,2,5,8]
print(solution.matchPlayersAndTrainers(players, trainers)) 