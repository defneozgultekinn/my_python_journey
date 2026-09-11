#lambda parameters: returned_expression
equation= lambda x,y: x+y*2
print(equation(2,4))
#we generally use lambda for functions that we are only gonna use once


#LAMBDA AND SORTED()
numbers = [5, 2, 9, 1]

result = sorted(numbers)
#it sorts the numbers in an increasing order
print(result)

fruits = ["apple", "watermelon", "tea", "mandarin"]

result = sorted(fruits)
#and with strings, alfabetical order
print(result)

#key tells Python:
# Which value should I use as the criterion when sorting the elements?
# The lambda function says:
# Give me a fruit name, and I will return the length of that name.

#sorted() performs the sorting.
# key specifies the criterion used for sorting.
# lambda extracts the sorting criterion from each element.

words = ["apple", "watermelon", "tea", "mandarin"]

result = sorted(words,  key=lambda word: len(word))
print(result)


students = [  ("Defne", 80),  ("Ali", 95),  ("Ece", 70)]
results= sorted(students, key=lambda result: result[1]  )  #the 1. index is the result
print(results)

#SORTING A DICTIONARY
pokemon_list = [
    {"name": "Pikachu", "power": 90},
    {"name": "Bulbasaur", "power": 45},
    {"name": "Charizard", "power": 100}
]
winner= sorted(pokemon_list, key=lambda pokemon: pokemon["power"], reverse=True) #to reverse the order
print(winner)

#IF-ELSE WITH LAMBDA
#lambda parameter: value_if_true if condition else value_if_false
get_status= lambda grade: "Passed" if grade>=18 else "Failed"
print(get_status(20))

# .SORT()
words = ["apple", "watermelon", "tea"]

words.sort( key=lambda word: len(word))     #.sort()  changes the list
print(words)

# MAP() AND LIST()
#list(map(lambda element: operation, iterable))
numbers = [10, 20, 30]
mapped_numbers= list(map(lambda number: number+2, numbers))   #does the same thing with a for loop
print(mapped_numbers)

# FILTER()
numbers2 = [1, 2, 3, 4, 5, 6]
selected_numbers= list(filter(lambda number: number%2==0, numbers2))
print(selected_numbers)



# map()    = transforms every element
# filter() = selects elements based on a condition
# list()   = converts the result into a regular list


sorted(collection, key=lambda element: sorting_value )
sorted(collection, key=lambda element: (first_criterion, second_criterion))

Değişkenlerin anlamları:

collection: Sıralanacak liste
element: O anda listenin içinden gelen tek bir eleman
sorting_value: O elemandan çıkaracağımız sıralama ölçütü