def is_valid_post_format(posts):
  # input: string -> parantheses, curly braces, and brackets ("()", "()[]{}")
  # output: bool -> true if tags are correctly formatted, false otherwise
  #
  # correct format: every opening tag has corresponding closed tag and closed in correct order
  # 
  # plan:

  # initalize a stack
  # iterate through the string
      # if it's a openening tag -> append to the stack
      # if it's a closing tag -> check if top of stack is the correct opening tag -> pop stack, otherwise return false

   # return true if stack is empty, false otherwise

   stack = []
   for char in posts:
      if (char == '(' or char == '[' or char == '{'):
         stack.append(char)
      elif char == ')':
         if stack[-1] == '(':
            stack.pop()
      elif char == ']':
         if stack[-1] == '[':
            stack.pop()
      elif char == '}':
         if stack[-1] == "{":
            stack.pop()
      
   return len(stack) == 0

def reverse_comments_queue(comments):
  # input: queue -> comments represented as a list of strings
  # output: stack -> reversed order of comments queue

  # plan:
  
  # initliaze a stack
  # iterate through comments queue
      # append current comment to stack

  # return stack

  stack = []
  list = []
  for comment in comments:
     stack.append(comment)

  for i in range(len(stack)):
     list.append(stack.pop())

  return list

def is_symmetrical_title(title):
   pass
   # input: string -> title of a post
   # output: bool -> true if title is symmetrical, false otherwise

   # Ignores spaces, punctuation, and case

   # plan:

   # lower the whole string

   # initalize a left pointer starting at the 1st index
   # initalize a right pointer starting at the last index
   
   # keep running while left is less than right:
      # if string[left] is a space or punction, move right by one
      # if string[right] is a space or punction, move left by one
      # if string[left] is equal to string[right] -> continue and move pointers inward
      # otherwise return false
   
   # return true

   title = title.lower()
   left = 0
   right = len(title) - 1

   while left < right:
      if title[left] == ' ' or title[left] == '!' or title[left] == '?' or title[left] == '.':
         left += 1
      if title[right] == ' ' or title[right] == '!' or title[right] == '?' or title[right] == '.':
         right -= 1
      if title[left] == title[right]:
         left += 1
         right -= 1
         continue

      return False
   
   return True

# def engagement_boost(engagements):
#     squared_engagements = [] # list of squared engagements
    
#     # iterate though enegagements, squaring each value, and appending it to the new list
#     for i in range(len(engagements)):
#         squared_engagement = engagements[i] * engagements[i]
#         squared_engagements.append((squared_engagement, i))
    
#     # sorts the squared engagements
#     squared_engagements.sort(reverse=True)
    
#     # creates an array of the same size of engagements
#     result = [0] * len(engagements)
#     # creates a pointer to the last position of the list
#     position = len(engagements) - 1
    
#     # iterates through squared engagements, stores that value into result[position] (starting from the end), and going backwards in the position
#     for square, original_index in squared_engagements:
#         result[position] = square
#         position -= 1
    
#     return result

def engagement_boost(engagements):
   pass
   squaredEngagements = []
   for i in range(len(engagements)):
      squared_engagement = engagements[i] * engagements[i]
      squaredEngagements.append((squared_engagement))
   
   left = 0
   right = len(squaredEngagements) - 1

   return squaredEngagements

   # while left < right:
   #    leftVal = squared_engagement[left]
   #    rightVal = squared_engagement[right]

      


print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))


  
