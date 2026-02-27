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

def tiggerfy(s):
   # input: string
   # output: new string with letters [t, i, g, e, r] removed from og string

   # question:
      # is it case sensitive? NO

   # plan

   # initialize array with values [t, i, g, e, r]
   # iterate through s:
      # if curr char is in arr, removes it
   
   # return new string

   arr = ['t', 'i', 'g', 'e', 'r']
   s = s.lower()

   for char in s:
      if char in arr:
         s = s.replace(char, "")

   return s

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))



