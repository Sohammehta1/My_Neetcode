
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        bucket  =[[] for _ in range(len(nums)+1)]
        ans = []
        for num in nums:
            freq[num] = 1 + freq.get(num,0) 
        for n,f in freq.items():
            bucket[f].append(n)
        # now we have our buckets
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                ans.append(n)
                if len(ans)==k:
                    return ans


        return ans