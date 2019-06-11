class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        temp = []
        count = 0
        for i in S:
            if i != '-':
                if 96 < ord(i) < 123:
                    i = chr(ord(i) - 32)
                temp.append(i)
                count += 1
        start = count % K
        if start != 0:temp2 = [''.join(temp[:start])]
        else:temp2 = []
        j = start
        while j < count:
            temp2.append(''.join(temp[j:j + K]))
            j += K
        return '-'.join(temp2)