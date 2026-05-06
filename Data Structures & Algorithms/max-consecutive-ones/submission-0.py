class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        i = 0
        while i != len(nums):
            if nums[i] == 0:
                if count > maxCount:
                    maxCount = count
                count = 0 
            else:
                count += 1 
            
            i += 1
        
        if count > maxCount:
            maxCount = count

        return maxCount
        