class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hungryStudents = len(students)
        countStudents = Counter(students)

        for sandwich in sandwiches:
            if countStudents[sandwich] > 0:
                hungryStudents -= 1
                countStudents[sandwich] -= 1
            else:
                break
        return hungryStudents










