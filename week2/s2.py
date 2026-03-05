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



species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))
