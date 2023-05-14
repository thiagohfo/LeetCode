class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
        first = ''
        second = ''
        target = ''

        for i in firstWord:
            first += str(letters[i])

        for i in secondWord:
            second += str(letters[i])

        for i in targetWord:
            target += str(letters[i])

        if int(first) + int(second) == int(target):
            return True
        else:
            return False