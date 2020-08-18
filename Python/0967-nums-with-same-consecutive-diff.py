class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
#         if N == 1:
#             return [i for i in range(10)]

#         ans = []
#         def DFS(N, num):
#             # base case
#             if N == 0:
#                 return ans.append(num)

#             tail_digit = num % 10
#             # using set() to avoid duplicates when K == 0
#             next_digits = set([tail_digit + K, tail_digit - K])

#             for next_digit in next_digits:
#                 if 0 <= next_digit < 10:
#                     new_num = num * 10 + next_digit
#                     DFS(N-1, new_num)

#         for num in range(1, 10):
#             DFS(N-1, num)

#         return list(ans)
        if N == 1:
            return [i for i in range(10)]

        # initialize the queue with candidates for the first level
        queue = [digit for digit in range(1, 10)]

        for _ in range(N-1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                # use set to avoid duplicates if tail is 0
                next_digits = set([tail_digit + K, tail_digit - K])

                for next_digit in next_digits:
                    if 0<= next_digit < 10:
                        new_num = 10 * num + next_digit
                        next_queue.append(new_num)

            # start the next level
            queue = next_queue

        return queue
