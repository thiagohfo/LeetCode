class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(num):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        return False
                return True
            else:
                return False

        count = 0
        for i in range(left, right + 1):
            temp = str(bin(i)[2:])
            count_1 = 0

            for j in temp:
                if j == '1':
                    count_1 += 1

            if is_prime(count_1):
                count += 1

        return count