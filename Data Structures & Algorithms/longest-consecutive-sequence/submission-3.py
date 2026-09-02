class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs1 = set(nums)
        print(hs1)
        ans = 0
        curr = 0
        for elm in nums:
            flag = 1
            curr = 0
            if elm-1 not in hs1:
                #this is the start
                while(flag == 1):
                    if elm+1 in hs1:
                        elm = elm+1
                        curr += 1
                    else:
                        flag = 0
                ans = max(ans,curr+1)
        return ans
        
             
            
                