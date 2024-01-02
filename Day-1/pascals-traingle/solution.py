class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def ncr(n, r):
             return fact(n) // (fact(r) * fact(n - r))
        def fact(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * fact(n - 1)
        r = []
        for i in range(numRows):
            o = []
            for j in range(i + 1):
                o.append(ncr(i, j))
            r.append(o)
        return(r)

                    
                    

                