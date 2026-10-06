class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min = 0

        for c in s:
            if c == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min += 1

        return min + open_brackets
        