class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        m = 0
        ls = len(s)
        for r in shift:
            direction, moves = r
            if direction == 1:
                m -= moves
                if abs(m) >= ls:
                    tmp = abs(m)
                    tmp %= ls
                    m = -tmp
            else:
                m += moves
                if m >= ls:
                    m %= ls
        # print(m)
        return s[m:] + s[:m]