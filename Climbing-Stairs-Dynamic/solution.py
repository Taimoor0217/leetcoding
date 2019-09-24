class Solution:
    hashmap = {}
    hashmap[0] = 0
    hashmap[1] = 1
    hashmap[2] = 2
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        try:
            val = self.hashmap[n]
            return val
        except:
            self.hashmap[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.hashmap[n]
            
            
            
        
# Runtime: 32 ms, faster than 89.40% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.6 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.