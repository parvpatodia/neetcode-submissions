class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for r in range(len(nums)):
            while len(dq) > 0 and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
        
        # 3. remove from front if that index is outside window
            if dq[0] < r - k + 1:
                dq.popleft()
            
            # 4. once window is full, record the max
            #    max is always at the front
            if r >= k - 1:
                result.append(nums[dq[0]])
        return result
                


