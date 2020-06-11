class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # firstCity = [i for i, j in costs]
        # diffCost = [j - i for i, j in costs]
        # return sum(firstCity) + sum(sorted(diffCost)[:len(costs)//2])

        costs.sort(key=lambda x: x[0]-x[1])
        
        n = len(costs) // 2
        cost = 0
        
        for i in range(n):
            cost += costs[i][0] + costs[i+n][1]
        
        return cost
        