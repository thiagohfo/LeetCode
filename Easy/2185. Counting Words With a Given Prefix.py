class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        import re
        count = 0

        for i in words:
            if re.findall(r'^{}'.format(pref), i):
                count += 1

        return count