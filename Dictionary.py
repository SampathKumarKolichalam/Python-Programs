profile={"name":"Sampath",
         "age":19,
         "rollno":38
         }
print(profile)            
print(profile.keys())#Printing keys of a key-value pair in dictionary.
print(profile.values())#Printing values of a key-value pair in dictionary.
print(profile["name"])#Accessing items in a dictionary.
print(len(profile))#finding length of a dictionary.
profile["name"]="Sampath kumar"#Updating values in adictionary.
print(profile)
profile["branch"]="cse"#Adding new items into a dictionary.
print(profile)
del profile["age"]#Deleting items in a dictionary.
print(profile)
del profile#Deleting the whole dictionary.
print(profile)