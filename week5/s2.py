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

# 4

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

# def halve_list(head):
#    pass
   # input: Node instance -> head of linked list (values all integers)
   # output: Node instance -> head of linked list, with all values halved by 2

   # Understand: Half all the values in a linked list

   # Plan:

   # iterate through the linked list:
      # at each nodes value, divide it by 2
   
   # return head

#    curr = head
#    while curr:
#       curr.value = curr.value / 2
#       curr = curr.next

#    return head

# node_one = Node(5)
# node_two = Node(6)
# node_three = Node(7)
# node_one.next = node_two
# node_two.next = node_three

# # Input List: 5 -> 6 -> 7
# print_linked_list(halve_list(node_one))

# 5

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

# def delete_tail(head):
#    pass
#    # input: Node instance -> head of linked list
#    # output: Node instance -> head of linked list

#    # Understand: Remove the last node in the linked list and return the list back

#    # Plan:

#    # Iterate through list while there's a curr.next.next value:
#    # once loop is done, curr.next = none

#    curr = head
#    while curr.next.next:
#       curr = curr.next
   
#    curr.next = None

#    return head

# butterfly = Node("Common Butterfly")
# ladybug = Node("Ladybug")
# beetle = Node("Scarab Beetle")
# butterfly.next = ladybug
# ladybug.next = beetle

# # Input List: butterfly -> ladybug -> beetle
# print_linked_list(delete_tail(butterfly))

# 6

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

# def find_min(head):
#    pass

#    # input: Node instance -> head of linked list
#    # output: int -> min mav in the linked list

#    # Understand: We want to find the min value in the linked list and return back to the user

#    # Plan:

#    # initalize a min with the heads value
#    # iterate through the link list:
#       # check if curr node value is less than the min -> if so update min to that val
   
#    # return min

#    min = head.value
#    curr = head.next

#    while curr:
#       if curr.value < min:
#          min = curr.value
#       curr = curr.next

#    return min

# head1 = Node(5, Node(6, Node(1, Node(8))))
# head2 = Node(8, Node(5, Node(6, Node(2))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_min(head1))

# # Linked List: 8 -> 5 -> 6 -> 7
# print(find_min(head2))

""" 7 """

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

def delete_item(head, item):
   pass
   # input: Node instance -> head of linked list, string -> item we're looking for in ll
   # output: Node instance -> head of linked list with node with value = item removed

   # edge case:
      # if no node can be found with .value = item, return list unchanged
   
   # Understand: Iterate through the linked list, when we find a node with a .value = item, we want to the previous node to point to the deleted nodes.next

   # plan:

   # if head value == item -> move head to be the next node and return new head
   # initalize a prev node pointing at the head, and a curr node pointing at head.next

   # iterate through linked list
   # if we find a node has a .value = item:
      # let prev node point curr.next node
      # return head
   # update the curr and prev node

   if head.value == item:
      head = head.next
      return head

   prev = head
   curr = head.next

   while curr:
      if curr.value == item:
         prev.next = curr.next
         return head
      curr = curr.next
      prev = prev.next
   
   return head

slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))

# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))

