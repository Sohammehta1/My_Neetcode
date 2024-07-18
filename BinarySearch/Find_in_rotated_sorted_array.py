class Solution:
    def findPivot(self,nums)->int:
        l= 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[l] <=nums[r]:
                return mid
            else:
                l =mid+1
    def BinarySearch(self,nums,target,l,r)->int:
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                l = mid+1
            else:
                r = mid-1
        return -1
    def search(self, nums: list[int], target: int) -> int:
        pivot = self.findPivot(nums)
        if nums[pivot] == target:
            return pivot
        sol1 = self.BinarySearch(nums,target,0,pivot-1)
        sol2 = self.BinarySearch(nums,target,pivot+1,len(nums)-1)
        if sol1 != -1:
            return sol1
        if sol2 != -1:
            return sol2
        return -1