class Solution:
    def pathInZigZagTree(self, label):
        if label == 1:
            return [1]
        level = Solution.get_level(label)

        if level % 2 == 0:
            pose = 2**level - 1 - label
        else:
            pose = label - 2**(level - 1)

        res = [label]

        print(level, pose)
        level -= 1
        while level > 0:
            pose //= 2
            if level % 2 == 0:
                start = 2**level - 1
                res.append(start - pose)
            else:
                start = 2**(level - 1)
                res.append(start + pose)
            level -= 1
        return res[::-1]

    @staticmethod
    def get_level(n):
        temp = bin(n)
        return len(temp[2:])


class Solution_best:
    def pathInZigZagTree(self, label):
        res = []

        while label:
            res.append(label)
            bl = label.bit_length()
            label ^= (1 << (bl - 1)) - 1
            label >>= 1
        res.reverse()
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.pathInZigZagTree(14))
