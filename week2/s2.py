def most_endangered(species_list):
   pass
   # input: list of dic -> each dic presents data associated w/ a species (name, habitat, and population)
   # output: string -> name of species w/ lowest population

   # edge case:
      # if there's multiple species w/ lowest population, return species w/ lowest index
   
   # plan

   # initialize dic w/ min species name and population
   # iterate through list:
      # at every species, get population, if it's less than curr min -> change dic name and population to that species

   # return species name

   dic = { "name": species_list[0]["name"], "population": species_list[0]["population"] }

   for i in range(1, len(species_list)):
      if species_list[i]["population"] < dic["population"]:
         dic["name"] = species_list[i]["name"]
         dic["population"] = species_list[i]["population"]
   
   return dic["name"]


def count_endangered_species(endangered_species, observed_species):
   # input: 
      # string endangered_species -> each char in string denotes a diff endangered species
      # string observed_species -> each char in string denotes a species observed in the region

   # output: int -> num of instances of observed species who are considered endangered

   # plan:
      
      # split up the endangered_species string into an array
      # intialize a counter

      # iterate through observed_species string:
         # if curr char is in endangered_species -> update the counter
      
      # return counter

   arr = list(endangered_species)
   counter = 0

   for species in observed_species:
      if species in arr:
         counter += 1
   
   return counter