class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        output = [1]*n
        for i in range(1,n):
            output[i]=nums[i-1]*output[i-1]
        # Now we have the prefixes
        postfix = 1
        for i in range(n-1,-1,-1):
            output[i] *=postfix
            postfix *= nums[i]
        return output

s = Solution()
print(s.productExceptSelf([1,2,3,4]))