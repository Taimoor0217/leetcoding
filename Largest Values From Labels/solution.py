class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        i = 0
        items = []
        while i < len(values):
            items.append((values[i] , labels[i]))
            i += 1
        items.sort(key=lambda tup: tup[0] , reverse = True)
        i = 0
        hashmap = {}
        SUM = 0
        while num_wanted and i < len(items):
            while hashmap.get(items[i][1] , 0) >= use_limit:
                i += 1
                if i >= len(items):
                    break
            if i < len(items):
                SUM += items[i][0]
                hashmap[items[i][1]] = hashmap.get(items[i][1] , 0) + 1
                i += 1
                num_wanted -= 1
        return SUM
# Runtime: 152 ms, faster than 41.88% of Python3 online submissions for Largest Values From Labels.
# Memory Usage: 17.8 MB, less than 100.00% of Python3 online submissions for Largest Values From Labels.