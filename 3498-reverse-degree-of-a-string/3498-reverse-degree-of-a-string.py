class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((26 - (ord(ch) - ord("a"))) * i for i, ch in enumerate(s, start=1))