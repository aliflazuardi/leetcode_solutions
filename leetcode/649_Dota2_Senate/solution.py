class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque()
        dq = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                rq.append(i)
            else:
                dq.append(i)

        step = len(senate)
        while len(rq) > 0 and len(dq) > 0:
            if rq.popleft() < dq.popleft():
                rq.append(step)
            else:
                dq.append(step)
            step += 1

        if len(rq) > 0:
            return "Radiant"
        return "Dire"
