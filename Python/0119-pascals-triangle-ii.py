class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
#         triangle = []

#         for row in range(rowIndex + 1):
#             sub = [None for _ in range(row + 1)]
#             sub[0], sub[-1] = 1, 1

#             for col in range(1,len(sub)-1):
#                 sub[col] = triangle[row - 1][col-1] + triangle [row-1][col]

#             triangle.append(sub)

#         return triangle [-1]

        res = [1]
        for i in range(rowIndex):
            for i in range(len(res)-1, 0, -1):
                res[i] += res[i-1]
            res.append(1)

        return res

