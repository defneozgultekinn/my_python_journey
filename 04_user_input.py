name= input ("Enter your name: ")
print("Hello "+ name + "!")
age= int(input("How old are you?: "))   #input always takes a str so if you want an int, you have to convert
next_year_age = age + 1
print(f"You'll be {next_year_age} next year")