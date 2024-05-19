# dict1={                     # dictionary => curly brackets{}
#     "key":"value",          # format for dict is "key":"value"
#     "name":"suhani",
#     "age":19,
#     64:10,
#     "name1":["suhani","manish","parmar"],           # in dict we can store list
#     "phone no.":("7984636865","9978819762")         # in dict we can store tuples
# }

# print(dict1)
# dict1["age"]=20            # dictionary is mutable 
# dict1["skills"]="coding"   # we can change or add a new value in dict
# print(dict1)

dict2={ 
    "name":"suhani",
    "marks":{                      #nested dict can also possible
        "DAA":60,
        "DBMS":55,
        "maths":58
    }
}
print(dict2)
print(dict2["marks"])
print(dict2["marks"]["DAA"])

print(dict2.keys())
print(list(dict2.keys()))
print(len(list(dict2.keys())))

#print(dict2["name2"])         #both are same but this will give error 
print(dict2.get("name2"))     #this will return none

new_dict={"name":"abc","fcfg":"guyg"}  #update the value of name and add also a new key and value
dict2.update(new_dict)
print(dict2)

d={
  "table":["a piece of furniture","list of facts & figures"],
  "cat":"a small animal"
}

sub={
    "python","java","c++","python","javascript","java","python","java","c++",'"c'
}
print(sub)
print(len(sub))
