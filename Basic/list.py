# list1=[12,"suhani",64,"parmar",25.36,"jay swaminarayan"] #list can store element of different data types
# # string->immutable(change not allowed)
# # list  ->muttable(change allowed)
# #e.g.
# list1[2]="manish"
# print(list1)

# list1.append("hello")
# print(list1)

# list2=[56,43,78,12,4,56]  

# list2.reverse() #reverse the list
# print(list2)

# list2.sort() #sort the list in ascending order
# print(list2)

# list2.sort(reverse=True) #sort the list in descending order
# print(list2)

# list3=["suhani","nirav","manish","shobhna"]    #sort function can only work with list of same data type
# list3.sort() 
# print(list3)

# list2.insert(2,'suhani') #insert element at index[ list.insert(index,ele) ]
# print(list2)

# movies=[]
# m1=input("enter 1st movie name : ")
# m2=input("enter 2nd movie name : ")
# m3=input("enter 3rd movie name : ")
# movies.append(m1)
# movies.append(m2)
# movies.append(m3)
# print(movies)

l1=[1,'suhu',64,'suhani',1]
l2=l1.copy()
l2.reverse()
if(l1==l2):
    print("string is palindrome")
else:
    print("strind is not palindrome")



