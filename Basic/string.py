str="suhani parmar"
print(str[1:6])  # forward indexing strats from 0
print(str[-6:-1])  # backward indexing strats from -1 and excluded end index
print(str[7:])  # consider as str[7:len(str)]
print(str[:5])  # consider as str[0:5] 
print(str[:])  # consider as str[0:len(str)]
print(len(str))
print("\n")


str1="i am a programmer"
strn=str1.endswith("er") #return true if string ends with "er" substring
print(strn)
str1=str1.capitalize() #capitalies 1st char
print(str1)  
str1=str1.removesuffix("er")
print(str1)
str2=str1.replace("programm","coder") # replace all occurences of old char/substr with new char/substr
print(str2)
stra=str1.find("a") # find index of 1st occuerence of chr/substr
print(stra)
print(str1.count("m")) #find no. of time occurence of char/substr
print(str1.count("mm"))
print("\n")


