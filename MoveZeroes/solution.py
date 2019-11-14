class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums)-1
        i = 0 ;
        flag = 0;
        while i <= j:
            # print (nums)
            # print ('i' , i , 'j' , j)
            if nums[i] is 0:
                k = i
                while k < j:
                    temp = nums[k+1]
                    nums[k+1] = nums[k]
                    nums[k] = temp
                    k+=1
                j -= 1
            if nums[i] != 0:
                i += 1
# Runtime: 884 ms, faster than 5.00% of Python3 online submissions for Move Zeroes.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Move Zeroes.