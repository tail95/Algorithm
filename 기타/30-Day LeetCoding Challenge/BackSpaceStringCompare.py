from collections import deque
class Solution:
    def convert(self, string):
        result = deque()
        for s in string:
            if s == "#":
                if result:
                    result.pop()
                continue
            result.append(s)
        return "".join(result)

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.convert(S) == self.convert(T)
