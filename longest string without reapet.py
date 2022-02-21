class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window principle 
        # abcabcbb abc --> get to a so remove a from set not substring bca...
        
        char = set()
        end = 0
        res = 0
        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[end])
                end += 1
            char.add(s[i])
            res = max(res, i - end + 1)
        return res
    
        # Recursive Solution 
   
        def dfs(s):
            if s=="":
                return 0
            unique = set(s)
            count  = 0
            for char in s:
                if char in unique:
                    unique.remove(char)
                    count+=1
                else:
                    break
            res = max(count, dfs(s[1:]))
            return res
        return dfs(s)