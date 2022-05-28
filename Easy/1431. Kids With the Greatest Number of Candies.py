class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cand = max(candies)
        answer = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_cand:
                answer[i] = True

        return answer