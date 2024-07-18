class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        remaining = {} # stores mapping of remaing sum for an element and it's index
        for i,n in enumerate(nums):
            if n in remaining:
                return [remaining[n],i]
            diff = target-n
            remaining[diff]=i
        

        