friends= ["Defne" , "Omer", "Andreas", "Giorgio"]
numbers= [5,8,3,4,5,6,7,2]

friends.extend(numbers)     #to combine 2 lists
print(friends)

friends2= ["Defne" , "Omer", "Andreas", "Giorgio"]
friends2.append("Zeynep")        #to add another element to the list
print(friends2)

friends2.insert(2, "Asu")
print(friends2)       #adding an element to a specific index

friends2.remove("Andreas")
print(friends2)

fruits=["apple", "grape", "melon"]
fruits.pop()
print(fruits)  #removes the last element of the list

print(fruits.index("apple"))
print(fruits.count("grape"))  #to count how many "grape"s are in that list


drinks=["spritz", "martini", "beer", "wine"]
print(drinks.sort())                  #this prints None; bc sort puts the list in alfab order in-place,
# so you have to sort the list, and then print it in a new line
drinks.sort()
print(drinks)

numbers.sort()     #if you .sort() a list with numbers->smaller to bigger
print(numbers)

numbers.reverse()    #reverse order
print(numbers)

numbers2 =numbers.copy()  #we copied the list
