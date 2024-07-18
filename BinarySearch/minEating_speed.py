import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        l = 1
        r=min_k= max(piles)
        # print(r)
        while l <=r:
            mid = (l+r)//2
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/mid)
            if hrs <= h:
                min_k = min(min_k,mid)
                r = mid-1
            else: 
                l = mid+1
        return min_k
                