class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:# i.e atleast 1 from remaining 2 numbers should be negative
                break
            if i> 0 and a == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l < r:
                three_sum = nums[l]+nums[r]+nums[i]
                if three_sum > 0:
                    r -=1
                elif three_sum < 0:
                    l +=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l +=1
                    r -=1
                    while nums[l]==nums[l-1] and l<r:
                        l +=1
        return res
        

        