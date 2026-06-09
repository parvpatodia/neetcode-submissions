class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 +nums2)
        middle = len(nums) % 2 
        mid = len(nums) // 2
        if middle  % 2 == 1:
            med = (math.ceil(mid))
            return(nums[med])
        else:
            return((nums[mid] + nums[mid -1])/2)