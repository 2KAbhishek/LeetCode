class Solution:
    def checkStraightLine(self, co: List[List[int]]) -> bool:
        if len(co) == 2:
            return True

        (x0, y0), (x1, y1) = co[: 2]
        dx, dy = x1 - x0, y1 - y0
        for x, y in co:
            if dx * (y - y1) != (x - x1) * dy:
                return False
        return True

