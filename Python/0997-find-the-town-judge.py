class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1: return 1

        countTrust = [0] * (N + 1)
        for tr in trust:
            countTrust[tr[0]] -= 1
            countTrust[tr[1]] += 1

        for person in range(N+1):
            if countTrust[person] == N-1: return person

        return -1

