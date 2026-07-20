class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0

        for char in s:
            if char == '(':
                left_min += 1
                left_max += 1
            elif char == ')':
                left_min -= 1
                left_max -= 1
            else:  # char == '*'
                left_min -= 1  # treating '*' as ')'
                left_max += 1  # treating '*' as '('

            # If max drops below 0, there are too many ')'
            if left_max < 0:
                return False

            # Minimum open parentheses cannot be negative
            if left_min < 0:
                left_min = 0

        # String is valid if min open count can reach 0 at the end
        return left_min == 0 