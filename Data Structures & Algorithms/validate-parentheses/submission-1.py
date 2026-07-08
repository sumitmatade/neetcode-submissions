class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            # Push opening brackets
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)

            # Check closing brackets
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if ch == ')' and top != '(':
                    return False
                if ch == ']' and top != '[':
                    return False
                if ch == '}' and top != '{':
                    return False

        return len(stack) == 0
        