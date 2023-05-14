class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        add = True

        for i in range(left, right + 1):
            str_num = str(i)
            add = True
            for j in str_num:
                if int(j) == 0:
                    add = False
                    break
                if i % int(j) != 0:
                    add = False
                    break

            if add:
                answer.append(i)

        return answer