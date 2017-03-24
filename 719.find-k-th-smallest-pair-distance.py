import heapq
from typing import List


# heap
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        heap = [(nums[i + 1] - nums[i], i, i + 1) for i in range(len(nums) - 1)]
        heapq.heapify(heap)

        d = 0
        for _ in range(k):
            d, root, nei = heapq.heappop(heap)
            if nei + 1 < len(nums):
                heapq.heappush(heap, (nums[nei + 1] - nums[root], root, nei + 1))

        return d


class Solution1:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            cnt, start = 0, 0
            for i in range(len(nums)):
                while nums[i] - nums[start] > mid:
                    start += 1
                cnt += i - start
            if cnt < k:
                left = mid + 1
            else:
                right = mid

        return left


solution = Solution()
print(solution.smallestDistancePair([1, 3, 1], 3))
