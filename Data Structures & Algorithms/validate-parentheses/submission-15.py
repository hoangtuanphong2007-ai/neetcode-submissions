class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        lst = []
        for i in range(len(s)):
            if s[i] == '(':
                lst.append(1)
            elif s[i] == '[':
                lst.append(2)
            elif s[i] == '{':
                lst.append(3)
            if len(lst) == 0: return False
            else:
                if s[i] == ')':
                    k = lst.pop()
                    if k != 1: return False
                elif s[i] == ']':
                    k = lst.pop()
                    if k != 2: return False
                elif s[i] == '}':
                    k = lst.pop()
                    if k != 3: return False
        return len(lst) == 0