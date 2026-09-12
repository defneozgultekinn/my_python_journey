#a function that calls itself from within helps to visualize a complex problem into basic steps, which
# be solved more easily iteratively or recursively

#ITERATIVE
def walk(step):
    for step in range(1,step+1):
        print(f"You've taken the step {step}")

walk(20)

#RECURSIVE
def countdown(number):
    if number == 0:
        print("Done!")     #base case
        return

    print(number)
    countdown(number - 1)

countdown(5)


def sum_numbers(num):
    if num==1:
        return 1

    return num+ sum_numbers(num-1)
result= sum_numbers(3)
print(result)

#def recursive_function(data):
    #fBase case
    #if simplest_condition:
    #    return simplest_result

    # Recursive case
    #return something + recursive_function(smaller_data)



#adding the numbers in a list
numbers = [10, 20, 30]
def sum_list(numbers):
    if numbers==[]:
        return 0
    first_num= numbers[0]
    remaining_num= numbers[1:]
    #return first_num+remaining_num   #we cant do this, first_n is an int, rem_num is a list
    return first_num+ sum_list(remaining_num)

result= sum_list(numbers)
print(result)


"""
Exercise: Check Whether a Number Exists in a List

Write a recursive function called contains_number() that:

- Receives a list of numbers and a target number.
- Returns True if the target exists in the list.
- Returns False if the target does not exist in the list.
- Must not use for loops, while loops, or the 'in' operator.
- Must make the list smaller in every recursive call.

Examples:

contains_number([4, 7, 2, 9], 2)
Returns: True

contains_number([4, 7, 2, 9], 5)
Returns: False

contains_number([], 3)
Returns: False
"""


def contains_number(numbers, target):
    if numbers==[]:
        return False
    first_number= numbers[0]
    remaining_numbers= numbers[1:]
    if first_number==target:
        return True
    return contains_number(remaining_numbers, target)   #contains_number([2, 3, 4], 3)
print(contains_number([1,2,3,4], 3))

    # Check whether the first number is equal to the target.

    # Otherwise, call the function again with the remaining list.


"""
Exercise: Count the Occurrences of a Number

Write a recursive function called count_number() that:

- Receives a list of numbers and a target number.
- Returns how many times the target appears in the list.
- Must not use for loops, while loops, count(), or the 'in' operator.
- Must make the list smaller in every recursive call.

Examples:

count_number([2, 5, 2, 8, 2], 2)
Returns: 3

count_number([2, 5, 8], 4)
Returns: 0

count_number([], 7)
Returns: 0
"""


def count_number(numbers, target):
    # Base case: What should be returned if the list is empty?
  if numbers==[]:
     return 0

  first_number = numbers[0]
  remaining_numbers = numbers[1:]
  if first_number== target:
      return 1+ count_number(remaining_numbers, target) #1 + the target number in our remaining list,
      # and the thing that counts that is our function
  else:
     return count_number(remaining_numbers,target)

result= count_number([1,2,3,4,4],4)    #THESE HAVE TO OUTSUDE OF THE FUNCTION!!
print(result)



    # If the first number equals the target:
    # Add 1 to the result of searching the remaining list.

    # Otherwise:
    # Return only the result of searching the remaining list.
