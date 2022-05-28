class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer = [0] * len(arr)

        for i in range(len(arr) - 1):
            answer[i] = max(arr[i + 1:])

        answer[-1] = -1

        return answer