class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        import re
        answer = []

        for i in words:
            if re.findall("^{}".format(i), s):
                answer.append(i)

        return len(answer)