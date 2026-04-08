class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)
        c = "".join(a)
        d = "".join(b)

        if c == d:
            return True
        else:
            return False
        