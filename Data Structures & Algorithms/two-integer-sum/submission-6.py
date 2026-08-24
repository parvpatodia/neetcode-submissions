class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                diff = target - nums[i]
                if diff == nums[j]:
                    return [i,j]

                