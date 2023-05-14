class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict_letters = {}

        for i in s:
            if i in dict_letters.keys():
                dict_letters[i] += 1
            else:
                dict_letters[i] = 1

        if max(dict_letters.values()) == min(dict_letters.values()):
            return True
        else:
            return False