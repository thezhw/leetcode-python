class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], base=2)


solution = Solution()
print(solution.reverseBits(43261596))
