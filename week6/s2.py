class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
   pass
   # Understand: We want to identify the value of each node that is a part of a cycle
      # input: Node instance -> head of linked list, representating the evidence list
      # output: String list -> each element being the value of the node that is a part of a cycle

   # Edge Case:
      # What if there is no cycle? -> return []
      # What if there's no list? -> return []
   
   # Plan

   # We have to make sure if there's even a cycle in the linked list
      # Do the 2 pointer technique to check if there's a cycle, if so -> continue, otherwise return []
   
   # In the 2nd pass, we have to check where the linked list cycle starts
      # We move one of the nodes to the head again, iterating 1 per node, where they meet is the start of the cycle

   # In the 3rd pass we append the values of each node after where the cycle starts up until we see it again

   if not evidence:
      return []
   
   slow = evidence
   fast = evidence

   while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

      if slow == fast:
         return check_cycle_start(evidence, slow)
   
   return []

def check_cycle_start(head, curr):
   while curr and curr.next:
      curr = curr.next
      head = head.next

      if curr == head:
         collect_false_evidence2(curr)

def collect_false_evidence2(cycle_start):
   false_evidence = []
   false_evidence.append(cycle_start.value)
   curr = cycle_start.next

   while curr != cycle_start:
      false_evidence.append(curr.value)
      curr = curr.next
   
   return false_evidence

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

