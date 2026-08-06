#we have a condition, if its true we do the task, if its not, we skip it

is_male= True
is_tall=False

if is_male and is_tall:
    print("He is handsome")
elif is_male and not(is_tall):
    print("Hello cutie")
else:
    print("He is ugly")

if is_male or is_tall:
    print("Maybe he is tall")
else:
    print("She is a woman")