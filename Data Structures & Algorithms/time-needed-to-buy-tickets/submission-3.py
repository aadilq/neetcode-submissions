class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()

        time = 0

        for i in range(len(tickets)):
            q.append(i)
        
        while q:
            currentPerson = q.popleft()

            time += 1

            tickets[currentPerson] -= 1
            if tickets[currentPerson] == 0:
                if currentPerson == k:
                    return time
            else:
                q.append(currentPerson)
        return time

        

