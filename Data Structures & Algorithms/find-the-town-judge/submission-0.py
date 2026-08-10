class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustPeople = [0] * (n + 1)

        for person1, person2 in trust:
            trustPeople[person1] -= 1
            trustPeople[person2] += 1
        for person in range(1, n + 1):
            if trustPeople[person] == n - 1:
                return person
        return -1