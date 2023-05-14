class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        reverse_str = ''

        for i in range(len(word)):
            if word[i] == ch:
                reverse_str = word[:i + 1]
                reverse_str = reverse_str[::-1]
                reverse_str += word[i + 1:]
                break

        if len(reverse_str) == 0:
            return word
        else:
            return reverse_str