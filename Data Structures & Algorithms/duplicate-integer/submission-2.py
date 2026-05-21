class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_2 = set(nums)
        nums_2 = list(nums_2)
        if len(nums_2) < len(nums):
            return True
        else:
            return False