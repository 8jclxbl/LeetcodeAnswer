class Solution:
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)

        total_gas = 0
        cur_gas = 0
        i = 0
        start = 0
        for i in range(length):
            cur_res = gas[i] - cost[i]
            total_gas += cur_res
            cur_gas += cur_res
            if cur_gas < 0:
                start = i + 1
                cur_gas = 0
        return start if total_gas >= 0 else -1

if __name__ == "__main__":
    s = Solution()
    test1 = [[5,1,2,3,4],[4,4,1,5,1]]
    test2 = [[1,2,3,4,5],[3,4,5,1,2]]
    test3 = [[3,3,4],[3,4,4]]
    print(s.canCompleteCircuit(*test3))