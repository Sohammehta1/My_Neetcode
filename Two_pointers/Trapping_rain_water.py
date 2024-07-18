class Solution:
    def trap(self, height) -> int: 
        l, r = 0,len(height)-1
        lMax =height[l]
        rMax =height[r]
        water_stored = 0
        while l<r:
            if lMax < rMax:
                l+=1
                lMax = max(lMax,height[l])
                water_stored += lMax-height[l]
            else:
                r -=1
                rMax = max(rMax,height[r])
                water_stored +=rMax-height[r]
                    

        return water_stored