def dfs(ans , digits , results , mapping):
    if not digits:
        results.append(ans)
    else:
        letters = mapping[digits[0]]
        remaining = digits[1:]
        for x in letters:
            dfs(ans+x , remaining , results , mapping)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",   
        }
        results = []
        if not digits:
            return []
        dfs("" , digits , results , mapping)
        return results

# Runtime: 28 ms, faster than 67.09% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.