class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = max(piles)   

        while left <= right:
            mid = left + (right - left) // 2
            hours = sum(math.ceil(p / mid) for p in piles)

            if hours <= h:
                result = mid      # mid works, record it, try smaller
                right = mid - 1
            else:
                left = mid + 1       # mid too slow, need faster

        return result