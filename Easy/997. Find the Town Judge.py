class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        voted = [0 for x in range(n + 1)]
        votes = [0 for x in range(n + 1)]

        if n == 1:
            return 1

        if len(trust) == 1:
            return trust[0][1]

        for pair in trust:
            voted[pair[1]] += 1
            votes[pair[0]] += 1

        if voted[voted.index(max(voted))] == (n - 1) and votes[voted.index(max(voted))] == 0:
            return voted.index(max(voted))
        else:
            return -1