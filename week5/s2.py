# 1

class Villager:
   def __init__(self, name, species, catchphrase):
      self.name = name
      self.species = species
      self.catchphrase = catchphrase
      self.friends = []

   def get_mutuals(self, new_contact):
      pass
      # input: Villager instance (new_contact)
      # output: list of strings -> representing name of all friends the curr villager and new_contact have in contact

      # Understand: We want to return a list of the names of villagers that self.friends and new_contact.friends have in common w/

      # plan:

      # initalize a list
      # iterate through new_contacts friends
      # if friend is in self.friends -> append to the list
      # return list

      lst = []
      for friend in new_contact.friends:
         if friend in self.friends:
            lst.append(friend.name)

      return lst
   
# bob = Villager("Bob", "Cat", "pthhhpth")
# marshal = Villager("Marshal", "Squirrel", "sulky")
# ankha = Villager("Ankha", "Cat", "me meow")
# fauna = Villager("Fauna", "Deer", "dearie")
# raymond = Villager("Raymond", "Cat", "crisp")
# stitches = Villager("Stitches", "Cub", "stuffin")

# bob.friends = [stitches, raymond, fauna]
# marshal.friends = [raymond, ankha, fauna]
# print(bob.get_mutuals(marshal))

# ankha.friends = [marshal]
# print(bob.get_mutuals(ankha))

# 2

class Node:
   def __init__(self, value, next=None):
      self.value = value
      self.next = next

# For testing
def print_linked_list(head):
   current = head
   while current:
      print(current.value, end=" -> " if current.next else "\n")
      current = current.next

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

print_linked_list(kk_slider)

# Add code here to link the above nodes
