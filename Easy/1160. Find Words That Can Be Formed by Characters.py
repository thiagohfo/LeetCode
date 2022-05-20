class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = Counter(chars)
        max_sum = 0

        for i in words:
            sum_len = True
            temp = Counter(i)

            for key, value in temp.items():
                if key in chars_dict.keys() and chars_dict[key] >= value:
                    pass
                else:
                    sum_len = False

            if sum_len:
                max_sum += len(i)
                sum_len = True

        return max_sum