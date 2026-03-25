# understand: instantiate 1 instance of an object Villager
# plan: Initalize "Apollo" with paremeters requiered for the class

""" apollo = Villager("Apollo", "Eagle", "pah")

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) """

''' UMPIRE template 
  # Understand 
inputs:
outputs:
constraints:
edge cases:

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )

  # Plan (pseudocode) 
  
  # Implement (python code)

  # Review (dry run of your code)

  # Evaluate (time and space complexity)
'''

# Understand: Instatiate an object with corresponding values and call the the greet_player() method

# bones = Villager("Bones", "Dog", "ruff it up")
# print(bones.greet_player("Mario"))

# 4.

class Villager:
   def __init__(self, name, species, personality, catchphrase, neighbor=None):
      self.name = name
      self.species = species
      self.personality = personality
      self.catchphrase = catchphrase
      self.furniture = []
      self.neighbor = neighbor

   def greet_player(self, player_name):
      return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
   def set_catchphrase(self, new_catchphrase):
      if len(new_catchphrase) >= 20:
         print("Invalid catchphase")
         return
      
      for char in new_catchphrase:
         if not char.isalpha() and not char.isspace():
            print(f"Invalid catchphase: {char}")
            return
      
      self.catchphrase = new_catchphrase
      print("Catchphrase updated")
   def add_item(self, item_name):
      valid_furniture = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
      if item_name in valid_furniture:
         self.furniture.append(item_name)
   def print_inventory(self):
      # input: void -> no input, however get's information from self.furniture
      # output: dic -> "item1: quantity, item2: quantity, item3: quantity"

      # edge case:
      # if player has no items, print "Inventory empty"

      # plan:
      
      # check if self.furniture is empty -> if so print "inventory empty" and return

      # initialize a dic
      # iterate through self.furniture:
         # for each item, add to dic if not already in it and add 1 to it
      
      # return dic

      if not self.furniture:
         print("Inventory empty")
         return
      
      dic = {}
      for furniture in self.furniture:
         if furniture not in dic:
            dic[furniture] = 0
         dic[furniture] += 1

      for furniture, value in dic.items():
         print(f"{furniture}: {value}")

def of_personality_type(townies, personality_type):
   pass
   # input: list of type Villager -> instances of class Villager, string -> persoanlity_type
   # output: list -> name of villagers w/ personality of personality_type

   # edge case:
   # if no villagers w/ a personality of personality_type -> return []

   # plan:

   # initalize a list
   # iterate through the townies:
      # if curr townie has a personality of personality_type -> append name to the list

   # return list

#    lst = []
#    for townie in townies:
#       if townie.personality == personality_type:
#          lst.append(townie.name)
   
#    return lst

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))

def message_received(start_villager, target_villager):
   pass
   # input: Villager -> start_villager, Villager -> target_villager
   # output: bool -> True if you can pass message from start_villager to target_villager, False otherwise

   # Understand: I have to make sure if a message can be passed from the start_neighbor to the target_neighbor using their neighbor attribute

   # Plan:

   # initalize a pointer being the curr villager:
   # loop until the curr villager is empty:
      # if curr villager is the target_villager -> return True
   
   # Return false since we didn't find the target even after iterating as far as we could

   curr_neighbor = start_villager
   while curr_neighbor:
      print(curr_neighbor.name)
      if curr_neighbor == target_villager:
         return True
      curr_neighbor = curr_neighbor.neighbor

   return False

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))










