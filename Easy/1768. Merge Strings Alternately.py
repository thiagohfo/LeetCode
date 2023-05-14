class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_total = len(word1) + len(word2)
        word = ''

        while (len(word) < len_total):
            if len(word1) > 0:
                word += word1[0]
                word1 = word1[1:]
            if len(word2) > 0:
                word += word2[0]
                word2 = word2[1:]

        return word