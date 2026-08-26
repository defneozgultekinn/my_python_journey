monthConvertions= {
    "Jan":"january",
    "Feb":"February",
    "Mar": "March",     #we have bunch of keys, and each key is assos with a value
}

print(monthConvertions["Mar"])
print(monthConvertions.get("Feb"))    #same thing
print(monthConvertions.get("Nov","Does not exist"))  #if a key isnt associated with a value,
# we can set a frase to print in case it doesnt exist, otherwise it will print out None