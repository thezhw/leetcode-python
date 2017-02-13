from typing import List


# 列表操作
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_dup_list = []
        for i in nums:
            if i not in no_dup_list:
                no_dup_list.append(i)
            else:
                no_dup_list.remove(i)

        return no_dup_list.pop()


# 哈希
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        no_dup_hash = {}
        for i in nums:
            try:
                no_dup_hash.pop(i)
            except KeyError:
                no_dup_hash[i] = 1

        return no_dup_hash.popitem()[0]


# 异或
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num

        return single


solution = Solution2()
print(solution.singleNumber([2, 2, 1]))
print(solution.singleNumber([4, 1, 2, 1, 2]))
