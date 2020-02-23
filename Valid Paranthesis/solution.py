class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        mapping = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        opening_braces = "{(["
        
        if (s[0] not in opening_braces) or (s[-1] in opening_braces):
            return False
        stack = []
        for b in s:
            if b in opening_braces:
                stack.append(mapping[b])
            else:
                try:
                    t = stack.pop()
                    if b is not t:
                        return False
                except:
                    return False
        
        return not stack


# Runtime: 28 ms, faster than 71.98% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.