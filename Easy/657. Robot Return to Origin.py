class Solution:
    def judgeCircle(self, moves: str) -> bool:
        list_moves = ['U', 'D', 'L', 'R']
        dict_moves = dict.fromkeys(list_moves, 0)

        for i in moves:
            if i == 'U':
                dict_moves['D'] -= 1
                dict_moves['U'] += 1
            if i == 'D':
                dict_moves['U'] -= 1
                dict_moves['D'] += 1
            if i == 'L':
                dict_moves['R'] -= 1
                dict_moves['L'] += 1
            if i == 'R':
                dict_moves['L'] -= 1
                dict_moves['R'] += 1

        if dict_moves['D'] == 0 and dict_moves['U'] == 0 and dict_moves['L'] == 0 and dict_moves['R'] == 0:
            return True
        else:
            return False