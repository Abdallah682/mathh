class Solution:
    def fib(self, n: int) -> int:
        res = 1 if n == 1 else 0
        if n <= 1:
            return res
        n1, n2 = 0, 1
        while n > 0:
            n1 = n2
            n2 = res
            res = n1 + n2
            n -= 1
        return res