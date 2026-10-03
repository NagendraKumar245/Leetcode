class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        for i in t:
            if i in freq:
                freq[i] -= 1
            else:
                return False
                
        for v in freq.values():
            if v != 0:
                return False
                
        return True
        