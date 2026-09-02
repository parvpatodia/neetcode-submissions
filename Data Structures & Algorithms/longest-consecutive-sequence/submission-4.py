class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs1 = set(nums)
        print(hs1)
        ans = 0
        curr = 0
        for elm in nums:
            curr = 0
            if elm-1 not in hs1:
                #this is the start
                while(True):
                    if elm+1 in hs1:
                        elm = elm+1
                        curr += 1
                    else:
                        break
                ans = max(ans,curr+1)
        return ans
        
             
            
                