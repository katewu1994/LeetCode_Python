class Solution:
    def romanToInt(self, s: str) -> int:
        value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        h = value.get(s[0])
        for n in s:
            ans += value.get(n)
            if h < value.get(n):
                ans -= 2 * h
            h = value.get(n)
        return ans