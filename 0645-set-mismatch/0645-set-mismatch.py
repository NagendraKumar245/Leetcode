class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0] * 2
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1

        for i in h:
            if h[i] == 2:
                ans[0] = i

        for i in range(1, len(nums) + 1):
            if i not in h:
                ans[1] = i

        return ans
        

        