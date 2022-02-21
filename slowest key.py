class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        duration = {l:0 for l in keysPressed}
        duration[keysPressed[0]] = releaseTimes[0]
        for i in range(1,len(releaseTimes)):
            time = releaseTimes[i] - releaseTimes[i-1]
            duration[keysPressed[i]] = max(duration[keysPressed[i]], time)
            
        duration = dict(sorted(duration.items(), key = lambda item : item[0], reverse = True))
        ans = ""
        maxVal = 0
        for key, val in duration.items():
            if val > maxVal:
                ans = key
                maxVal = val
        return ans