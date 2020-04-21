class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashmap = {}
        count = 0 
        for a in arr:
            hashmap[a] = 1
        for a in arr:
            count += hashmap.get(a+1 , 0)
        return count