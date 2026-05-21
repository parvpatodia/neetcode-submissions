class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        directory = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in directory:
                return [directory[diff], i]
            directory[n] = i

