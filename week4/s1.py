# def extract_nft_names(nft_collection):
#    pass
#    # input: list of dictionary -> "name": "x", "creator": "y", "value": "x"
#    # output: list of all NFT names

#    # match: dictionaries and arrays
   
#    # plan:

#    # initialize an array to store nft names
#    # loop over nft collection 
#       # at each nft, extract name and append to the list

#    # return list

#    list = []
#    for nft in nft_collection:
#       list.append(nft["name"])

#    return list

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

def identify_popular_creators(nft_collection):
   pass

   # input: list of dictionaries -> "name": "x", "creator": "y", "value": "x"
   # output: list of populator creators

   # A creator is popular if they have created more than 1 NFT in the collection

   # edge case:
      # 1. If no creators have created more than 1 NFT -> return []
   
   # match: dictionaries -> used to track number of times that creator has showed up

   # plan:
      # initialize an empty dic
      # iterate through the nfts in the nft collection:
         # extra the nft's creator
         # add creator to the dictionary if not already in it
         # add 1 to dic[creator]
      
      # extract all the creators from dic with a value greater than 1 and add them to a list

      # return list of popular creators

   dic = {}
   for nft in nft_collection:
      creator = nft["creator"]
      if creator not in dic:
         dic[creator] = 0
      dic[creator] += 1

   return [creator for creator, count in dic.items() if count > 1]
        
# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]

# nft_collection_2 = [
#     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
#     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
#     {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
# ]

# nft_collection_3 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# print(identify_popular_creators(nft_collection))
# print(identify_popular_creators(nft_collection_2))
# print(identify_popular_creators(nft_collection_3))

def average_nft_value(nft_collection):
   pass
   # input: list of dictionaries -> "name": "x", "creator": "y", "value": "x"
   # output: int -> average value of the NFT collection

   # Edge case:
      # if empty -> return 0
   
   # plan:

   # return 0 if list nft_collection is empty
   # initialize a sum value
   # iterate through the nft collection
      # extra the value of each nft, adding it to the sum

   # return sum / length of the nft_collection

   if not nft_collection:
      return 0
   
   sum = 0
   for nft in nft_collection:
      sum += nft["value"]
   
   return sum / len(nft_collection)

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]
# print(average_nft_value(nft_collection))

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
#     {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
# ]
# print(average_nft_value(nft_collection_2))

# nft_collection_3 = []
# print(average_nft_value(nft_collection_3))




