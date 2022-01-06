class Solution:
    def countBits(self, n: int) -> List[int]:
        l = [0] * (n+1)
        for i in range(n + 1):
            if i % 2 == 0:
                l[i] = l[i>>1]
            else:
                l[i] = l[i>>1] + 1
        return l
            