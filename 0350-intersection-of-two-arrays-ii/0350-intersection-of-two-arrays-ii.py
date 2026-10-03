class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq={}
        for num in nums1:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        lst=[]
        for num in nums2:
            if num in freq and freq[num]>0:
                lst.append(num)
                freq[num]-=1
        return lst