class Solution_base:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        self.base = [i for i in range(1, m + 1)]
        res = []
        for i in queries:
            res.append(self.search(i))
        return res

    def search(self, val):
        for index, value in enumerate(self.base):
            if value == val:
                break

        for i in range(index, 0, -1):
            self.base[i], self.base[i - 1] = self.base[i - 1], self.base[i]
        return index


class Solution:
    def processQueries(self, queries, m):
        self.base = {val: index for index, val in enumerate(range(1, m + 1))}
        res = []
        for i in queries:
            tmp = self.base[i]
            res.append(tmp)
            for key, val in self.base.items():
                if val < tmp:
                    self.base[key] += 1
            self.base[i] = 0
        return res
