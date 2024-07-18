class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        countS,countT = {},{}

        for i in range(n):
            countS[s[i]] =1+ countS.get(s[i],0) # 0 is the default value if the key is not found
            countT[t[i]] =1+ countT.get(t[i],0)
        return countS==countT