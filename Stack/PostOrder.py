class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t[0]=='-' and len(t)>1:
                temp = int(t[1:])
                print(temp)
                stack.append(-1*temp)
            elif t.isnumeric():
                stack.append(int(t))
            else:
                a,b = stack.pop(),stack.pop()

                result = 0
                if t =="*":
                    stack.append(a*b)
                elif t =="+":
                    stack.append(a+b)
                elif t =="/":
                    stack.append(int(b/a))
                else:
                    stack.append(b-a)
            print(stack)
        return int(stack.pop())
                