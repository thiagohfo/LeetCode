class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic_code = {}
        word = ''

        for i in range(len(s)):
            dic_code[indices[i]] = s[i]

        indices.sort()

        for i in indices:
            word += dic_code[indices[i]]

        return word