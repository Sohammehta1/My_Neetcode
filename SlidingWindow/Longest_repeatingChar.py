class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r = 0,1
        max_length = 1
        substring = set()
        substring.add(s[l])
        max_length = 1
        while l < len(s) and r <len(s):
            max_length = max(max_length,len(substring))
            if s[r] in substring:
                while l< r and s[r] in substring:
                    substring.remove(s[l])
                    l +=1
                
            else:
                substring.add(s[r])
                r +=1
        max_length = max(max_length,len(substring))
        return max_length


        