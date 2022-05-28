class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        answer = []
        odd = []

        for i in nums:
            if i % 2 == 0:
                answer.append(i)
            else:
                odd.append(i)

        for i in odd:
            answer.append(i)

        return answer