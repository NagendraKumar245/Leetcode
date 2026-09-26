class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i,n in enumerate(nums):
            if target==n:
                return i
        return -1



if __name__=="__main__":
    print(Solution().search(nums = [4,5,6,7,0,1,2], target = 0)) 
    print(Solution().search(nums = [4,5,6,7,0,1,2], target = 3)) 
    print(Solution().search(nums = [1], target = 0)) 
        