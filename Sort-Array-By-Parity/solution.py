class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        array1 = []
        array2 = []
        
        for x in A:
            if x % 2:
                array2.append(x)
            else:
                array1.append(x)
        return array1 + array2
# Runtime: 96 ms, faster than 57.39% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.5 MB, less than 5.19% of Python3 online submissions for Sort Array By Parity.