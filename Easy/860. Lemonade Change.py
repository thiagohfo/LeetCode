class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}
        exit = True

        for i in bills:
            if i == 5:
                change[i] += 1
            elif i == 10:
                change[i] += 1

                if change[5] >= 0:
                    change[5] -= 1
                else:
                    return False
            elif i == 20:
                change[i] += 1
                tip = 15

                while tip > 0:
                    if change[10] > 0:
                        change[10] -= 1
                        tip -= 10

                    if change[5] > 0:
                        change[5] -= 1
                        tip -= 5
                    else:
                        return False

        return exit