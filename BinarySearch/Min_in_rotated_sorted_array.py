class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums)-1
        min_ele = float('inf')
        while l<=r:
            mid = (l+r)//2
            temp = nums[mid]
            min_ele = min(min_ele,temp)
            if temp >= nums[l] and temp >=nums[r]:
                if nums[l] > nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            elif temp >=nums[l] and temp <=nums[r]:
                r = mid-1
            elif temp <=nums[l] and temp >=nums[r]:
                r = mid-1
            else:
                r = mid-1
        return min_ele