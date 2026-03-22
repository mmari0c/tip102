def collect_festival_points(points):
   pass
   # input: stack -> each item representing points from a single booth
   # output: int -> sum of points collected after visiting all booths

   # plan:

   # initalize a sum
   # loop while there's still something in the stack:
      # pop item in stack and add it to the sum
   
   # return the sum

   sum = 0
   while points:
      sum += points.pop()

   return sum


def booth_navigation(clues):
   # input: list -> order to visit the booths
      # ex. [1, 2, "back", 3, 4], when "back", backtrack to previous booth
   # output: list -> final sequence of booths visited

   # match: stacks, since we will be backtracking

   # edge case:
      # 1. If we have 2 backs at the same time w/ an empty stack, we should not perform anything

   # plan:

   # initialize a stack
   # iterate through the clues list:
      # if it's "back", then we pop the stack
      # otherwise, we append the integer to the stack
   
   # return the stack

   stack = []
   for clue in clues:
      if not clue == "back":
         stack.append(clue)
      else:
         if stack:
            stack.pop()
   
   return stack

def merge_schedules(schedule1, schedule2):
   # input: 2 strings -> each char corresponds to a performance slot
   # output: string -> merged schedules in alternating order starting w/ schedule1

   # edge case:
      # 1. A string is longer than the other -> append additional performances onto the end of merged schedule

   # happy case: schedule1 = "abc" schedule2 = "pqr" -> apbqcr
   # odd case: schedule1 = "ab" schedule2 = "pqrs" -> apbqrs

   # plan:

   # initalize an empty string
   # initalize a left1 and left2 value of 0
   
   # iterate len(schedule1) times
      # appending schedule1[left1] and then schedule2[left2]
      # incrementing by left1 and left2 by 1

   # return string
   result = []
   left1, left2 = 0, 0

   while left1 < len(schedule1) and left2 < len(schedule2):
      result.append(schedule1[left1])
      result.append(schedule2[left2])
      left1 += 1
      left2 += 1

   result.append(schedule1[left1:])
   result.append(schedule2[left2:])

   return "".join(result)

def next_greater_event(schedule1, schedule2):
  pass
  # input:
   # 1. int array -> each index representing an event's popularity score (subset of schedule2)
   # 2. int array -> each index repreenting an event's popularity score

  # output: array (len(schedule1)) -> for each event in schedule1, each index is the next event in schedule2 w/ a higher popularity score

  # edge case:
   # 1. if there's no event such that the next event in schedule2 is higher to the current event in schedule1 -> -1

   
  # plan:

  #