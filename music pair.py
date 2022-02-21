class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # 0. base case: if there are less than 2 songs, return 0
        if len(time) < 2:
            return 0
        # 1. set up an empty hashmap for the songs, and an answer array as 0
        hashmap = {}
        answer = 0
        # 2. go thru each song
        for song in time:
            # 2.1 if the song is evenly divisible by 60, add however many values there are like that starting from 0 to answer, and add 1 to hashmap[60]
            if song % 60 == 0:
                answer += hashmap.get(60, 0)
                hashmap[60] = hashmap.get(60, 0) + 1
            # 2.2 if the remainder of song % 60 is in the hashmap, add however many songs like that starting from 0 to answer, then add 1 to hashmap[60 - song % 60] to use as the next remainder
            elif song % 60 in hashmap:
                answer += hashmap.get(song % 60, 0)
                hashmap[60 - song % 60] = hashmap.get(60 - song % 60, 0) + 1
            # 2.3 if the remainder is not in the hashmap, add 1 to hashmap[60 - song % 60]
            else:
                hashmap[60 - song % 60] = hashmap.get(60 - song % 60, 0) + 1
        
        # 3. return the answer
        return answer