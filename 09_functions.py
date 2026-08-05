#A FUNCTION IS A COLLECTION OF CODE, WHICH PERFORMS A SPECIFIC TASK
def say_hi():
    print("Hello User")

print("Top")
say_hi()
print("Bottom")


def fruit(fruit_name):
    print("I love " + fruit_name)
#WE CAN GIVE THE FUNC AN INFO AND DEPENDING ON THAT INFO, IT CAN PERFORM THE TASK A BIT DIFFERENTLY
fruit("apple")


def you(name, age):
    print("hello " + name + " you are " + str(age))

you("defne", 21)