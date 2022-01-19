class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        curr = 0
        
        for i in range(len(nums)):
            curr = str(nums[i])
            print(curr) #testing
            if len(curr) % 2 == 0:
                count += 1
        return count