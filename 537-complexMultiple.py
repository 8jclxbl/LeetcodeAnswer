class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        ar,av = Solution.trans(a)
        br,bv = Solution.trans(b)
        
        r = ar * br - av * bv
        v = ar * bv + br * av
        
        return "{}+{}i".format(r,v)
    
    @staticmethod
    def trans(complex_):
        r,v = complex_.split('+')
        
        if r[0] == '-':
            rv = -1 * int(r[1:])
        else:
            rv = int(r)
            
        if v[0] == '-':
            vv = -1 * int(v[1:-1])
        else:
            vv = int(v[:-1])
            
        return rv,vv
        