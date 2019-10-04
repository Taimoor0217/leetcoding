class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        index = 0
        if len(nums1) == 0:
            result = nums2
        elif len(nums2) == 0:
            result = nums1
        else:
            s1 = nums1[0]
            s2 = nums2[0]
            a1 = nums1
            a2 = nums2
            if s1 > s2:
                a2 = nums1
                a1 = nums2
            for x in a2:
                while index < len(a1) and  a1[index] < x :
                    result.append(a1[index])
                    index += 1
                result.append(x)
            if index < len(a1):
                result += a1[index:]
        length = len(result)
        n = int(length/2)
        if length % 2 != 0:
            return result[n+1-1]
        else:
            return (result[n] + result[n-1])/2
            
# Runtime: 120 ms, faster than 21.26% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.