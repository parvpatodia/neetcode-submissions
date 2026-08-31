class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []
        # for i in range(len(nums)):
        #     prod = 1 
        #     for j in range(len(nums)):
        #         if j != i:
        #             prod = prod * nums[j]
        #     result.append(prod)
        # return result
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        finresult = []
        for i in range(len(nums)):
            if i == 0:
                prefix[0]  = 1
            else:
                prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            if i == len(nums):
                suffix[-1] = 1
            else:
                suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(len(nums)):
            result = prefix[i] * suffix[i]
            finresult.append(result)
        return finresult
