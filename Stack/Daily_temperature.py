class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        n = len(temperatures)
        ans = [0]*n 
       
        for i in range(n-1,-1,-1):
            temp = temperatures[i]
            while stack:
                a = stack.pop()
                if temp < a[0]:
                    ans[i] = a[1]- i
                    stack.append(a)
                    break
                
            
            stack.append([temp, i]) 
            print(stack)       
            
                
        return ans
