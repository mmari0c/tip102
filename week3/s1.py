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

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
  
