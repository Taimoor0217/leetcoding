class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        i = 0 
        for x in strs:
            val = ''.join(sorted(x))
            # for y in x:
            #     val = val * ord(y)
            # val = str(val)
            n = hashmap.get(val , [])
            n.append(strs[i])
            hashmap[val] = n
            i += 1
        return hashmap.values()
# Runtime: 100 ms, faster than 94.43% of Python3 online submissions for Group Anagrams.
# Memory Usage: 16.2 MB, less than 49.06% of Python3 online submissions for Group Anagrams.
