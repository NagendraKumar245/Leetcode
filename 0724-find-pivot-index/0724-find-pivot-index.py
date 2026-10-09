class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefixsum=[0]*len(nums)
        prefixsum[0]=nums[0]
        for i in range(1,len(nums)):
            prefixsum[i]=prefixsum[i-1]+nums[i]
        total=prefixsum[-1]
        for i in range(len(nums)):
            ls=prefixsum[i]-nums[i]
            rs=total-prefixsum[i]
            if ls==rs:
                return i
        return -1