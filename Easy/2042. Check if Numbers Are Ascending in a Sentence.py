class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [str(x) for x in range(1, 100)]
        text = s.split(' ')
        result = []
        numbers_str = []

        for i in text:
            if i in numbers_str:
                return False

            if i in numbers:
                numbers_str.append(i)
                result.append(int(i))

        result_sorted = sorted(result)

        if result == result_sorted:
            return True
        else:
            return False