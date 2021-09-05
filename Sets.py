"""profile_set={"Sampath",19,38,"khammam"}
print(profile_set)#1st Run.
print(len(profile_set))
print(profile_set)#2nd Run.
profile_set.add("SRH")#Adding item to a set.
print(profile_set)
profile_set.remove("khammam")#Removing a value/item/element from a set.
print(profile_set)
del profile_set
print(profile_set)"""
set1={4,5,6,9}
set2={1,2,5,6,8}
print("intersection",set1&set2)
print("union",set1|set2)
print("Difference",set1-set2)