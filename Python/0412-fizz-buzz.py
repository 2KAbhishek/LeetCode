class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for num in range(1,n+1):
            if num % 15 == 0:
                out.append("FizzBuzz")
            elif num % 5 == 0:
                out.append("Buzz")
            elif num % 3 == 0:
                out.append("Fizz")
            else:
                out.append(str(num))

        return out

