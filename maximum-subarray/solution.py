class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        # ---------- Divide and Conquer ---------------
        def foo(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0] , nums[1] , nums[0]+nums[1])

            mid = len(nums)-1//2
            left_sum = 0
            right_sum = 0

            for i in range(0 , mid):
                left_sum = max(nums[i] , nums[i]+ left_sum )

            for i in range(mid+1 , len(nums)):
                right_sum = max(nums[i] , nums[i]+ right_sum )

            ans = max(
                left_sum + right_sum,
                foo(nums[0:mid+1]),
                foo(nums[mid+1:])
            )
            return ans
        return foo(nums)
        
