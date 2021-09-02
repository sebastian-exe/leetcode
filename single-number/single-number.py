class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 0
        
        for k,v in d.items():
            if v is 0:
                return k