class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count_students = 0

        for i in range(len(startTime)):
            if endTime[i] == queryTime:
                count_students += 1
            elif startTime[i] > queryTime:
                continue
            elif endTime[i] > queryTime:
                count_students += 1

        return count_students