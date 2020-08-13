class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            sub = [None for _ in range(row + 1)]
            sub[0], sub[-1] = 1, 1

            for col in range(1, len(sub) - 1):
                sub[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

            triangle.append(sub)

        return triangle

