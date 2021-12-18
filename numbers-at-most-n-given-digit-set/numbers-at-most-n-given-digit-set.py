class Solution:
    def atMostNGivenDigitSet(self, D: List[str], n: int) -> int:
        m, N = len(D), str(n)
        ln = len(N)
        res = sum(m ** i for i in range(1, ln ))
        print(res)
        i = 0
        while i < ln:
            res += sum(d < N[i] for d in D) * m ** (ln-1-i)
            if N[i] not in D:
                break
            i += 1
            
        return int(res) + (i == ln)