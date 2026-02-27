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

words = ["christopher", "robin", "milne", "hello"]
s = "crm"
print(is_acronym(words, s))