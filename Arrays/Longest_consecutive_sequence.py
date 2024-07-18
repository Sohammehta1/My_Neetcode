class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hash_set = set(nums)
        longest_seq = 0
        for n in nums:
            if (n-1) not in hash_set:
                temp = n
                seq_count =0
                while temp in hash_set:
                    seq_count +=1
                    temp +=1
                longest_seq = max(longest_seq,seq_count)

        return longest_seq


            