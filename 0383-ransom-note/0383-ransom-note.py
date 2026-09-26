class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq={}
        for i in magazine:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        for i in ransomNote:
            if i in freq and freq[i]>0:
                freq[i]-=1
            else:
                return False
        return True
        