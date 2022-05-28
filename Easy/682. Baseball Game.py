class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []

        for i in ops:
            if i != 'C' and i != 'D' and i != '+':
                scores.append(int(i))
            elif i == 'C':
                scores.pop()
            elif i == 'D':
                scores.append(scores[-1] * 2)
            elif i == '+':
                scores.append(scores[-1] + scores[-2])

        return sum(scores)