class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = s.lower()
        i = 0
        j = len(s) - 1

        while i  < j:
            while i < j and not p[i].isalnum():
                i += 1
            while i < j and not p[j].isalnum():
                j -= 1
            if p[i] != p[j]:
                return False
            i += 1
            j -= 1
        
        return True
