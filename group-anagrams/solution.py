class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for x in strs:
            k = ''.join(sorted(x))
            n = results.get(k , [])
            if n:
                n.append(x)
            else:
                n = [x]
            results[k] = n
        return results.values()
        
        