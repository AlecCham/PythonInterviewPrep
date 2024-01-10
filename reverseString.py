class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        reversestr = " ".join(reversed(A.split()))
        return reversestr

A = " Hello world"

s = Solution()

print(s.solve(A))
