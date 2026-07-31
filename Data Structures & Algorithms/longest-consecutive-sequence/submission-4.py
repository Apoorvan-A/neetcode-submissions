class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums=set(nums)
        lcs=0
        for i in set_nums:
            if i-1 not in set_nums:
                length=0
                while(i+length) in set_nums:
                    length+=1
                lcs=max(lcs,length)
        return lcs