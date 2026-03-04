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

def max_audience_performances2(audiences):
   maxVal = max(audiences)
   count = audiences.count(maxVal)

   return maxVal * count

def num_popular_pairs(popularity_scores):
   pass

   # input: array of ints -> represent popularity score of songs
   # output: int -> num of popular song pairs
      # num of pairs = (n * n-1)/2

   # plan

   # create a dic
   # iterate through popularity_scores:
      # if score is not in dic -> add it to dic
      # add 1 to value of dic[score]
   
   # create num of pairs variable
   # iterate through values in new dic:
      # at each value, calculate (val * val-1) / 2 and add to num_of_pairs
   
   # return num_of_pairs

   dic = {}
   for score in popularity_scores:
      if score not in dic:
         dic[score] = 0
      dic[score] += 1
   
   num_of_pairs = 0
   for value in dic.values():
      num_of_pairs += (value * (value - 1))/2
   
   return num_of_pairs
   



