from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_dup_list = []
        for i in nums:
            if i not in no_dup_list:
                no_dup_list.append(i)
            else:
                no_dup_list.remove(i)

        return no_dup_list.pop()


solution = Solution()
print(solution.singleNumber([2, 2, 1]))
print(solution.singleNumber([4, 1, 2, 1, 2]))
