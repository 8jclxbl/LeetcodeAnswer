class Solution:
    def groupThePeople(self, groupSizes):
        res = {}
        for index, value in enumerate(groupSizes):
            if value not in res:
                res[value] = [index]
            else:
                res[value].append(index)
        result = []
        key_list = sorted(res.keys())
        for key in key_list:
            val = res[key]
            lg = len(val)
            if lg == key:
                result.append(val)
            else:
                num = lg // key
                start = 0
                for i in range(num):
                    result.append(val[start:start + key])
                    start += key
        return result
