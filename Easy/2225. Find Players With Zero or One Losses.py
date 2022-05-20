class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict_w = {}
        dict_l = {}
        result = [[], []]

        for pair in matches:
            if pair[0] in dict_w.keys():
                dict_w[pair[0]] += 1
            else:
                dict_w[pair[0]] = 1

            if pair[1] in dict_l.keys():
                dict_l[pair[1]] += 1
            else:
                dict_l[pair[1]] = 1

        for i in dict_w.keys():
            if i not in dict_l.keys():
                result[0].append(i)

        for i in dict_l.keys():
            if dict_l[i] == 1:
                result[1].append(i)

        result[0].sort()
        result[1].sort()

        return result
