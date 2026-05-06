class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        # i = 0
        for i in tokens:
            if i not in "+-*/":
                ans.append(int(i))
            else:
                a = int(ans.pop())
                b = int(ans.pop())
                if i == "+":
                    c = a + b
                    ans.append(c)
                elif i == "-":
                    c = b - a
                    ans.append(c)
                elif i == "*":
                    c = b * a
                    ans.append(c)
                elif i == "/":
                    c = int(b / a)
                    ans.append(c)
        

        return ans[-1]
               





        