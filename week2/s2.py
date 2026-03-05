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

def navigate_research_station(station_layout, observations):
   # input: 
      # string station_layout -> each char represents diff observation points
      # string observations -> each char represents order we want to make observations
   
   # output: int -> total time taken to visit all requiered observation points in the given order

   # note:
      # we can only move from one point to another
      # time taken to move from one observation to another is = | i - j |
   
   # plan

   # create a dic: char -> index (from station_layout)

   # initialize curr_pos = index of observations[0] in station_layout  ← physical starting position
   # initialize total_time = curr_pos

   # iterate through observations starting at index 1:
   #   next_pos = dic[observations[i]]
   #   total_time += | curr_pos - next_pos |
   #   curr_pos = next_pos  ← update physical position

   # return total_time

   dic = {}
   for i, char in enumerate(station_layout):
      dic[char] = i
   
   curr_pos = dic[observations[0]]
   total_time = curr_pos

   for i in range(1, len(observations)):
      next_pos = dic[observations[i]]
      total_time += abs(curr_pos - next_pos)
      curr_pos = next_pos
   
   return total_time

def prioritize_observations(observed_species, priority_species):
   # input: 
      # list priority_species -> distinct species that are priority
      # list observed_species -> species observed in which are a superset of priority_spcies

   # output:
      # list -> sorted list of observed_species such that the relative ordering of times in observed_species matches that of priority_species
   
   # note:
      # species that don't appear in priority_species should be placed at the end in ascending order

   # plan

   # initialize dic -> key: species, value: num of times species have been observed
   # initalize an empty list

   # iterate through priority_species;
      # append curr_species dic[curr_species] times
   
   

   dic = {}
   for species in observed_species:
      if species not in dic:
         dic[species] = 0
      dic[species] += 1
   
   lst = []
   for species in priority_species:
      lst.extend([species] * dic[species])

   newLst = []
   for species in observed_species:
      if species not in priority_species:
         newLst.extend([species] * dic[species])

   newLst.sort()
   lst.extend(newLst)

   return(lst)

def distinct_averages(species_populations):
   # input: list -> of even len, each element represents population of a species
   # output: int -> num of distinct avgs calculate using the below process:

   # while list is not empty:
      # find min and remove it from list
      # find max and remove it from list
      # calc avg population between min & max
   
   # plan

   # initialize list of avgs
      # while list is not empty:
      # find min and remove it from list
      # find max and remove it from list
      # calc avg population between min & max
      # append avg to list
   
   # convert list to set

   # return len of set

   arr = []
   while species_populations:
      maxVal = max(species_populations)
      species_populations.remove(maxVal)

      minVal = min(species_populations)
      species_populations.remove(minVal)

      arr.append((minVal + maxVal) / 2)
   
   setOfArr = set(arr)

   return len(setOfArr)

def max_species_copies(raised_species, target_species):
   # input: 
   # string raised_species -> represents list of species available to release (each char represents a diff species)
   # string target_species -> represents specific sequences of species you want to form and release together

   # output: int -> num of copies of target_spcies that can be formed by taking species from raised_species and rearranging them

   # test:
      # raised_species = "abcba"
      # target_species = "abc"

      # output -> 1, since we can only form abc once. We have "a" and "b" left but no "c" to construct another one
      # we can only release the min number of raised_species that are target_species
   
   # plan:

      # create a new dic -> key: each in target_species, value: num of that species in raised species

      # iterate through target species:
         # create a dic key for each
      
      # iterate through raised species:
         # if raised species is in dic:
            # add 1 to it
      
      # return min value of dic

   dic = {}
   for species in target_species:
      dic[species] = 0
   
   for species in raised_species:
      if species in dic:
         dic[species] += 1
   
   maxNumOfCopies = min(dic.values())

   return maxNumOfCopies

raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2
   


   
