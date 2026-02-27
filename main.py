def final_value_after_operations(operations):

   tigger = 1
	
   for operation in operations:
      if operation == 'bouncy' or operation == 'flouncy':
         tigger += 1
      else:
         tigger -= 1

   return tigger

def can_pair(item_quantities):
   # input: List of numbers
   # output: Bool. True -> if each number in list is even, False otherwise

   # plan

   # iterate through list
   # if curr num is not even, return false
   # at the end, return true

   for item in item_quantities:
      if item % 2 != 0:
         return False
      
   return True

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))

