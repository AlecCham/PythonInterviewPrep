class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        A = list(A)
        A.sort()
        major = A[len(A) // 2]
        return major


major = Solution()

maj = major.majorityElement( (2, 1, 2, 5, 5, 5))
print(maj)
