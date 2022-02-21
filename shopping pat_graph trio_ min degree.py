class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # Time Complexity: O(|E|* |V|)
        # Space Complexity: O(|E|)
        deg = Counter()
        adj = defaultdict(set)
        for (a, b) in edges:
            deg[a] += 1
            deg[b] += 1
            if a < b:
                adj[a].add(b)
            else:
                adj[b].add(a)
        mutual = defaultdict(set)
        ans = float('inf')
        for a in range(1, n + 1):
            for b in adj[a]:
                intersect = [x for x in adj[a].intersection(adj[b]) if x > b]
                for c in intersect:
                    ans = min(ans, deg[a] + deg[b] + deg[c] - 6)
        return ans if ans < float('inf') else -1