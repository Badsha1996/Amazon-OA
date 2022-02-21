class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        d = {word:0 for word in words}
        for word in words:
            if word in d:
                d[word]+=1
        d = dict(sorted(d.items(), key = lambda item : item[1], reverse = True))
        res = []
        for key in d.keys():
            if k==0:
                break
            res.append(key)
            k-=1
        return res