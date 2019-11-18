class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for n in nums:
            count = hashmap.get(n , 0)
            hashmap[n] = count+1
        vals = sorted(list(hashmap.items()) ,reverse = True, key=operator.itemgetter(1))[:k]
        # print (vals)
        data = []
        for n in vals:
            data.append((-1)*(-1)*n[0])
        return data
        
        
                
                
#Runtime: 112 ms, faster than 88.22% of Python3 online submissions for Top K Frequent Elements.
#Memory Usage: 17.2 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
