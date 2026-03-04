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

def max_audience_performances(audiences):
   pass
   
   # create a new dic -> key: num of people val: how many performances had that number of audiences
   # iterate through audiences
      # if val is not in dic -> add it to dic
      # add 1 at dic[value]
   
   # return the max val * its value

   dic = {}
   for audience in audiences:
      if audience not in dic:
         dic[audience] = 0
      dic[audience] += 1

   maxVal = max(dic)
   
   return maxVal * dic[maxVal]

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))


