class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        points_in = [0] * len(queries)

        for i in range(len(queries)):
            p1 = queries[i][0]
            p2 = queries[i][1]
            r = queries[i][2]
            for j in points:
                d = (((p1 - j[0]) ** 2) + ((p2 - j[1]) ** 2)) ** (1 / 2)
                if d ** 2 <= r ** 2:
                    points_in[i] += 1

        return points_in