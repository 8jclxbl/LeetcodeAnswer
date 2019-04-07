"""
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
返回重复了 N 次的那个元素。

由于确定了其中只有N+1个不同元素，所以只要出现了两次就是那个元素
"""

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dic = {}
        for i in A:
            if i not in dic:
                dic[i] = 1
            else:
                return i