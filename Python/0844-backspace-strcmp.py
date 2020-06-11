class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stkS, stkT = [], []

        def genStk(stack, string):
            for char in string:
                if char != '#':
                    stack.append(char)

                elif stack:
                    stack.pop()
            return stack

        return genStk(stkS, S) == genStk(stkT, T)

