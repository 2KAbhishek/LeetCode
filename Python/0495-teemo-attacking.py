class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        totalDur = 0

        if (len(timeSeries) == 0):
            return totalDur

        for i in range(1,len(timeSeries)):
            totalDur += min(duration, (timeSeries[i] - timeSeries[i-1]))


        return totalDur + duration
