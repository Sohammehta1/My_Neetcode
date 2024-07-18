
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        freq =[]
        for num in nums:
            if num in freq:
                return True
            else:
                freq.append(num)
        return False
