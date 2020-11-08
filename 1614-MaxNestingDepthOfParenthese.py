import collections


class Solution_base:
    def maxDepth(self, s: str) -> int:
        stack = []
        cnt = 0
        max_cnt = 0
        for i in s:
            if i == "(":
                stack.append("(")
                cnt += 1
            if i == ")":
                stack.pop()
                cnt -= 1
            if cnt > max_cnt:
                max_cnt = cnt
        return max_cnt


class Solution:
    def maxDepth(self, s: str) -> int:
        stack = collections.deque()
        cnt = 0
        max_cnt = 0
        for i in s:
            if i == "(":
                stack.append("(")
                cnt += 1
            if i == ")":
                stack.pop()
                cnt -= 1
            if cnt > max_cnt:
                max_cnt = cnt
        return max_cnt
