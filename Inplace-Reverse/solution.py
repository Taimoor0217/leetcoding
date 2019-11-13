class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0 
        j = len(s) -1
        while j > i :
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i +=1 
            j -= 1
# Runtime: 216 ms, faster than 95.96% of Python3 online submissions for Reverse String.
# Memory Usage: 17.3 MB, less than 97.67% of Python3 online submissions for Reverse String.
