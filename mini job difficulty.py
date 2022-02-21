class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        Here dp[i] represents the minimum difficulty of a job schedule if we start today at i-th job and finish at some later job j ignoring what happens before i. Therefore, today we perform jobs from i to j, which costs us max(jobs[i], jobs[i+1], ..., jobs[j]) plus the cost of performing the rest of the jobs, which is given by dp[j+1]. We want to choose the optimal number of jobs to perform today, thus we check all possible j from i to number_of_jobs - day (because we need to have at least one job to perform at each of remaining days).

Repeating this procedure for each day we finally arrive at the final dp, where dp[0] represents the best jobs schedule if we start from the jobs[0], i.e. exactly what we need.
        '''
        n = len(jobDifficulty)
        if n < d: return -1
        dp = [float("inf")] * n + [0]
        
        for day in range(d):
            for i in range(n - day):
                maxd, dp[i] = 0, float("inf")
                for j in range(i, n - day):
                    maxd = max(maxd, jobDifficulty[j])
                    dp[i] = min(dp[i], maxd + dp[j+1])
                    
        return dp[0]