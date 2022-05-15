class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        new_list = []
        count = 0
        letter = ''

        for i in range(len(s)):
            if letter == s[i]:
                count += 1
            else:
                letter = s[i]

                if count > 2:
                    new_list.append([i - count, i - 1])

                count = 1

            if i == (len(s) - 1):
                if count > 2:
                    new_list.append([i - (count - 1), i])

        return new_list
