class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        import re
        lens = [len(word) for word in words]
        index = lens.index(min(lens))
        letters = []

        min_word = words[index]

        for i in min_word:
            add = True
            for j, word in enumerate(words):
                if word == min_word:
                    continue
                else:
                    if i not in word:
                        add = False
                    else:
                        words[j] = re.sub(i, '_', words[j], 1)

            if add:
                letters.append(i)

        return letters