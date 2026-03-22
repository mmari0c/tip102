def extract_nft_names(nft_collection):
   pass
   # input: list of dictionary -> "name": "x", "creator": "y", "value": "x"
   # output: list of all NFT names

   # match: dictionaries and arrays
   
   # plan:

   # initialize an array to store nft names
   # loop over nft collection 
      # at each nft, extract name and append to the list

   # return list

   list = []
   for nft in nft_collection:
      list.append(nft["name"])

   return list



