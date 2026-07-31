print("Start \nDoing it")  #dividing the string to the next line

phrase= "Crazy Lunapark"  #storing a sting in a variable
print(phrase)
print (phrase + " is fun")
print(phrase.lower())  #makes the string all lower case
print(phrase.upper())  #makes the string all upper case
print(phrase.isupper())   #True/False
print(phrase.upper().isupper()) #True
print(phrase.count("a")) #to see how many a's there are

print(len(phrase))
print(phrase[2]) #getting the index 2 char
print(phrase.index("n")) #learning the index of n
print(phrase.replace("Crazy","Fun")) # changes it to Fun Lunapark
