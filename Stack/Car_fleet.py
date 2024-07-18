class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleets = 0
        pairs = [[p,s] for p,s in zip(position,speed)]
        pairs = sorted(pairs, key = lambda x : x[0])
        stack = []
        for p,s in pairs[::-1]:
            if stack:
                t1 = stack.pop()
                t = (target-p)/s
                stack.append(t1)
                if t > t1 : # which means no collision
                    stack.append(t)
            else:
                stack.append((target-p)/s)
               
                
                 
        return len(stack)