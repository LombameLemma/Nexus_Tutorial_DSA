import math
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = math.gcd(a, b)
        count = 0
        for x in range(1, g + 1):
            if g % x == 0:
                count += 1   
        return count
