class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for x in nums:
            val = hash_map.get(x , 0) + 1
            if val > 1 :
                return True
            else:
                hash_map[x] = val
        return False
        
# Runtime: 136 ms, faster than 93.13% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 20.1 MB, less than 7.55% of Python3 online submissions for Contains Duplicate.