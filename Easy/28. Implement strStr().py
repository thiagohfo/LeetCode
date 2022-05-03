class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        len_needle = len(needle)
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i + len_needle] == needle:
                    index = i
                    break
            return index
        else:
            return -1