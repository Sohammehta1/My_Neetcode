class Solution:
    def maxArea(self, heights: list[int]) -> int:
        max_water =-1
        l,r = 0,len(heights)-1
            
        while l < r:
            min_ht = min(heights[l], heights[r])
            max_water = max(max_water, min_ht*(r-l))
            if heights[l] > heights[r]:
                r-=1
            else:
                l +=1 

        return max_water
        