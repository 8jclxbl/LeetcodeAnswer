class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = []
        for i in S:
            if i == '#':
                if not s_stack:continue
                s_stack.pop()
            else:
                s_stack.append(i)
        
        t_stack = []
        for i in T:
            if i == '#':
                if not t_stack:continue
                t_stack.pop()
            else:
                t_stack.append(i)
                
        if s_stack == t_stack:
            return True
        else:
            return False