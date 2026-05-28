class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        have = {}
        satisfied, required = 0, len(need)
        result = ""
        l = 0

        for r in range(len(s)):
            have[s[r]] = have.get(s[r], 0) + 1
            if s[r] in need and have[s[r]] == need[s[r]]:
                satisfied += 1
            
            while satisfied == required:
                if result == "" or (r - l + 1) < len(result):
                    result = s[l:r+1]
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    satisfied -= 1
                l += 1

        return result
