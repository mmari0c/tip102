# 5

def best_set(votes):
   pass
   # input: dic -> key: attendees id num val: artist they voted for ex. 1234: "SZA"
   # output: string -> artist w/ highest num of votes

   # edge case:
      # 1) if tie -> return any artist
   
   # plan

   # create dic -> key: artist val: num of votes that artist has
   # iterate through votes:
      # if that artist in not in our new dic -> add them to it
      # add 1 vote to artist
   
   # return artist with max votes

   dic = {}
   for artist in votes.values():
      if artist not in dic:
         dic[artist] = 0
      dic[artist] += 1
   
   return max(dic, key=dic.get)

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
