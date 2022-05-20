class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = []
        new_text = text.split()

        for i in new_text:
            add = True
            for j in brokenLetters:
                if j in i:
                    add = False
                    break

            if add:
                words.append(i)

        return len(words)