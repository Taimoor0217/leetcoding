class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        i = 0
        for x in nums:
            hash_map[x] = i
            i += 1
        i = 0
        for x in nums:
            index = hash_map.get(target - x , -1)
            if index != -1 and i != index:
                return [i , index]
            i += 1
            
# Runtime: 68 ms, faster than 44.09% of Python3 online submissions for Two Sum.
# Memory Usage: 15.7 MB, less than 5.11% of Python3 online submissions for Two Sum.