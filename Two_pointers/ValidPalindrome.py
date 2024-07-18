import re
class Solution:
    def isalphaNum(self, c:chr):
        temp= ord(c)
        return (ord('A') <=temp <= ord('Z') or ord('a')<=temp<=ord('z') or ord('0')<=temp<=ord('9')) 
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l <=r:
            if not self.isalphaNum(s[l]):
                l +=1
                continue
            if not self.isalphaNum(s[r]):
                r -=1
                continue
            
            if s[l].lower()==s[r].lower():
                l +=1
                r-=1
            else:
                return False
        return True
                
            