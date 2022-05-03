class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        array_bool = []
        letters = ''
        first_word = ''

        if len(strs[0]) > 0:
            first_word = strs[0]
        else:
            return ''

        for ind, i in enumerate(first_word):
            array_bool = []

            for j in strs[1:]:
                if ind < len(j) and i == j[ind]:
                    array_bool.append(True)
                else:
                    array_bool.append(False)
                    break

            if False not in array_bool:
                letters += i
            else:
                return letters

        return letters