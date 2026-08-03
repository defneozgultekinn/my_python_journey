drinks= ["Tea", "Coke", "Water"]
print(drinks[2])  #to reach a specific element of the list, we use the index of it
friends= ["Defne" , "Omer", "Andreas", "Giorgio"]
print(friends[-2])
print(friends[1:]) #this will grab the index 1 element and all of the elements after that
print(friends[1:3]) #from index 1 to index 3 NOT including 3

#if you want to change an element:
friends[2]="Stella"
print(friends)