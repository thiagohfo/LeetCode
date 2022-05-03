class Solution:
    def isValid(self, s: str) -> bool:
        esquerda = {'(': 1, '[': 2, '{': 3}
        direita = {')': 1, ']': 2, '}': 3}
        stack = []
        grew = False

        for i in s:
            if i in esquerda.keys():
                stack.append(i)
                grew = True
            elif i in direita.keys() and len(stack) > 0:
                inde = esquerda[stack[-1]]
                indd = direita[i]

                if inde == indd:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if (len(stack) == 0) and (grew == True):
            return True
        else:
            return False