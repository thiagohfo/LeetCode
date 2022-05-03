class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        counts = [0] * len(boxes)

        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j] == '1' and i != j:
                    counts[i] += abs(j - i)

        return counts
