class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        nums_sorted = sorted(nums)

        diff,ans = 0,0
        for i in range(1,len(nums_sorted)):
            if nums_sorted[i] - nums_sorted[i-1] == 1:
                diff += 1
            elif nums_sorted[i] - nums_sorted[i-1] == 0:
                continue
            else:
                ans = max(ans, diff+1)
                diff = 0
        ans = max(ans, diff+1)
        return ans

             
            
                