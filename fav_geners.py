import collections
def favor(userSongs, songGenres):
    output={}
    for i in userSongs:
        list=userSongs[i]
        count=collections.defaultdict(int)
        for song in list:
            for genre,songs in songGenres.items():
                if song in songs:
                    count[genre]+=1

        output[i]=[key for key,val in count.items() if val ==max(count.values())]
    return output

userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

print(favor(userSongs, songGenres))