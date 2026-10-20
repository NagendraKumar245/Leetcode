class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        line = [0] * 102
        points_on_line = 0

        for s,e in nums:
            line[s] += 1
            line[e + 1] -= 1

        for i in range(1, 102):
            line[i] += line[i - 1]
            if line[i] != 0:
                points_on_line += 1

        return points_on_line