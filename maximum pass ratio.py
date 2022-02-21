class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # idea find where is the maximum increamtent of the final ratio
        # let f(x) = (a+x)/(b+x) 
        # Then at x = 0 , del f = f(x+1) - f(x) = (b-a)/(b**2+b) is the increasement of the ratio
        # Using Heap to find out the maximum assignment of each extraStudents
        passRatioList = [[(-b+a)/(b**2+b),a,b] for a,b in classes] #use  - del f we can find the maximum increasement
        heapq.heapify(passRatioList)
        
        while extraStudents>0:
            _ , a , b = heapq.heappop(passRatioList)
            if _==1:
                return 1.0
            a , b = a+1 , b+1
            extraStudents -= 1
            heapq.heappush(passRatioList,[(-b+a)/(b**2+b),a,b])
            
        ans = 0
        for _,a,b in passRatioList:
            ans += a/b
        return ans/len(passRatioList)