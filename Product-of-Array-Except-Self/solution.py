class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return [nums[1] , nums[0]]
        i = len(nums) -2
        temp = len(nums)*[None]
        temp[-1] = nums[-1]
        while i > -1 :
            temp[i] = nums[i] * temp[i+1]
            i -=1
        i = 1
        while i < len(nums):
            nums[i] *= nums[i-1]
            i += 1
        
        output = len(nums)*[None]
        output[0] = temp[1]
        output[len(nums)-1] = nums[len(nums)-2]
        i = 1
        
        while i < len(nums)-1:
            output[i] = nums[i-1]*temp[i+1]
            i +=1
        
        return output

# Runtime: 160 ms, faster than 9.76% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 22.5 MB, less than 6.00% of Python3 online submissions for Product of Array Except Self.
