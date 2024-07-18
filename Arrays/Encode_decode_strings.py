class Solution:

    def encode(self, strs: list[str]) -> str:
        if len(strs)==0:
            return None
        return '|'.join(strs)
         

    def decode(self, s: str) -> list[str]:
        if s==None:
            return []
        return s.split('|')
