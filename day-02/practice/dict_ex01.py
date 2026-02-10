info = {

    "name" : "Shubham bhaiya", #str
    "city" : "Pune", # str
    "qualification" : "Mtech",
    "age" : 29, # int
    "salary" : 22.5,  # float
    "married" : True, # bool
    "favourites" : ["teaching", "movies", 18] # list
  
  }

print("I live in",info["city"])
print("I love", info.get("favourite", "Not found"))
info.update({"channel" : "TrainWithShubham"})
print(dir(info))

# iterate a dictionary
for key,values in info.items():
    print(key,values) 