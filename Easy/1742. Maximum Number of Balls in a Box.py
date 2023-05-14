class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def num(num_t):
            sum_total = 0
            num_str = str(num_t)

            for i in num_str:
                sum_total += int(i)

            return sum_total

        boxes = {}

        for i in range(lowLimit, highLimit + 1):
            num_temp = num(i)

            if num_temp in boxes.keys():
                boxes[num_temp] += 1
            else:
                boxes[num_temp] = 1

        num_max = max(boxes.values())

        return num_max