from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen, seen[0] = [False] * len(rooms), True
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)

        return all(seen)


solution = Solution()
print(solution.canVisitAllRooms([[1], [2], [3], []]))
