def is_acronym(words, s):
   # input: list of words, string s
   # output: Bool: True -> if s in an acronym of words, False otherwise

   # Happy case: words = ["Chris", "Robin", "milne"] s = "crm" -> True, because each char in s matches with the 1st letter each item in the array in order

   # Question: Is the s case sensitive -> NO

   # plan:

   # iterate through enumarated words list:
      # check if curr_word[0] is != to s[i] -> return False
   
   # return True
   if len(words) != len(s):
      return False

   for i, word in enumerate(words):
      if word[0] != s[i]:
         return False
   
   return True

def make_divisible_by_3(nums):
   # input: list of nums
   # output: int: Min num of operations to make all elements divisible by 3

   # Note: Can only add or sub 1 from any element of nums in 1 operation

   # Plan

   # Int counter: number of operations performed
   # iterate through each num in nums:
      # for each num:
         # if num % 3 == 0:
            # continue through loop
         # elif num == 1 -> count += 2
         # else:  
            # add 1 to counter

   counter = 0
   for num in nums:
      if num % 3 == 0:
         continue
      else:
         counter += 1
   
   return counter
         