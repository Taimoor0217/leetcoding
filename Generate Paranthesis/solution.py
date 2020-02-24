class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def dfs(ans = "" ,left_count=0 , right_count=0):
            if len(ans) is 2*n:
                results.append(ans)
            else:
                if left_count < n:
                    dfs(ans+'(' , left_count+1 , right_count)
                if right_count < left_count:
                    dfs(ans+')', left_count , right_count + 1)
        dfs()
        return results
# Runtime: 32 ms, faster than 72.06% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Generate Parentheses.