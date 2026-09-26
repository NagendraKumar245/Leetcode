from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = set()
        duplicates = set()
        total_sum = 0
        
        for num in nums:
            if num not in seen:
                seen.add(num)
                total_sum += num
            elif num not in duplicates:
                duplicates.add(num)
                total_sum -= num
                
        return total_sum