class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = [0] * len(s)

        for i, value in enumerate(s):
            if value == c:
                continue
            else:
                distances = []
                for j in range(i + 1, len(s)):
                    if s[j] == c:
                        distances.append(abs(j - i))
                        break

                for j in range(i - 1, -1, -1):
                    if s[j] == c:
                        distances.append(abs(j - i))
                        break

                answer[i] = min(distances)

        return answer