class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        paranthesis = []
        stack = []
        def rec_generation(openP: int,closeP: int):
            if openP < n:
                stack.append('(')
                rec_generation(openP+1, closeP)
                stack.pop()
            if closeP < openP:
                stack.append(')')
                rec_generation(openP, closeP+1)
                stack.pop()
            if openP ==closeP == n:
                paranthesis.append(''.join(stack))
        rec_generation(0,0)
        return paranthesis

            