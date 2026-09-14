class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in closeToOpen:
                if stk and stk[-1] == closeToOpen[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        
        return True if not stk else False
        