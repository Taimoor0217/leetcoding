class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def LCS(s1 , s2 , i , j):
            if memo.get((i,j) , -1) != -1:
                return memo[(i,j)]
            if i < 0 or j < 0:
                memo[(i,j)] = 0
                return 0
            elif s1[i] == s2[j]:
                memo[(i,j)] = 1 + LCS (s1 , s2 , i-1 , j-1)
                return memo[(i,j)]
            elif s1[i] != s2[j]:
                memo[(i,j)] =  max(
                    LCS (s1 , s2 , i , j-1),
                    LCS (s1 , s2 , i-1 , j),
                )
                return memo[(i,j)]
        reverse = s[::-1]
        return LCS(s , reverse , len(s)-1 , len(s)-1)

# Runtime: 3016 ms, faster than 12.49% of Python3 online submissions for Longest Palindromic Subsequence.
# Memory Usage: 453 MB, less than 7.69% of Python3 online submissions for Longest Palindromic Subsequence.
