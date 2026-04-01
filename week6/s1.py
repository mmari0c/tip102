# 1

"""
  # Understand 

inputs: No input
outputs: Break everything down into multiple lines (does the same exact thing)
constraints: N/A
edge cases: N/A

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )

  # Plan (pseudocode) 
  
  # Implement (python code)

  # Review (dry run of your code)

  # Evaluate (time and space complexity)
"""
# class SongNode:
#     def __init__(self, song, next=None):
#         self.song = song
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print(current.song, end=" -> " if current.next else "")
#         current = current.next
#     print()
        

# top_hits_2010s = SongNode("Uptown Funk")
# node2 = SongNode("Party Rock Anthem")
# node3 = SongNode("Bad Romance")

# top_hits_2010s.next = node2
# node2.next = node3

# print_linked_list(top_hits_2010s)

""" 2 """

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
   pass
   """
   # Understand: return a dic that maps each artist in list to its frequency 
   # { artistName: n}

   inputs: Linked list -> each node having a song and artist
   outputs: Dic -> artist with it's frequency
   constraints: N/A
   edge cases: Empty ll -> return {}

   # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )

   # Plan (pseudocode)

   create a new dic
   iterate through the linked list
      get artist name, if artist not in dic -> add them to dic
      add 1 to dic[artist]

   return dic 
   
   # Implement (python code)

   # Review (dry run of your code)

   # Evaluate (time and space complexity)
   """

   if not playlist:
       return {}

   dic = {}
   curr = playlist

   while curr:
      if curr.artist not in dic:
          dic[curr.artist] = 0
      dic[curr.artist] += 1
      curr = curr.next

   return dic

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))



       
       
