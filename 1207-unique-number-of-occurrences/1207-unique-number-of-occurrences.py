from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = [0] * 2001
        for num in arr:
            freq[num + 1000] += 1
        seen_counts = set()
        
        for count in freq:
            if count > 0:
                if count in seen_counts:
                    return False
                seen_counts.add(count)
                
        return True  