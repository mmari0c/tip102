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

# class Node:
#    def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# # For testing
# def print_linked_list(head):
#    current = head
#    while current:
#       print(current.value, end=" -> " if current.next else "\n")
#       current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle

# print_linked_list(kk_slider)

# 3

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def add_first(head, task):
#    pass
   # input: node instance -> head of a linked list, string -> new task we want to add to the front of linked list
   # output: node instance -> new head of linked list

   # understand: Create a new node with it's value being the task passed to the function, we then want to append that new node to the front of linked list and return the new node, now being the head

   # plan:

   # create a new instance of Node with a value = task
   # append that new Node at the front of list
      # new node points to the curr head
   # return new Node

#    new_task = Node(task)
#    new_task.next = head

#    return new_task

# task_1 = Node("shake tree")
# task_2 = Node("dig fossils")
# task_3 = Node("catch bugs")
# task_1.next = task_2
# task_2.next = task_3

# # Linked List: shake tree -> dig fossils -> catch bugs
# print_linked_list(add_first(task_1, "check turnip prices"))






