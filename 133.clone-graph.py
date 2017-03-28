"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
import collections

from public.Node import Node


# DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def dfs(node):
            if not node:
                return
            if node in visited:
                return visited[node]
            clone = Node(node.val, [])
            visited[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)


# BFS
class Solution1:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def bfs(node):
            if not node:
                return
            clone = Node(node.val, [])
            visited[node] = clone
            queue = collections.deque()
            queue.append(node)
            while queue:
                top = queue.popleft()
                for n in top.neighbors:
                    if n not in visited:
                        visited[n] = Node(n.val, [])
                        queue.append(n)
                    visited[top].neighbors.append(visited[n])

            return clone

        return bfs(node)
