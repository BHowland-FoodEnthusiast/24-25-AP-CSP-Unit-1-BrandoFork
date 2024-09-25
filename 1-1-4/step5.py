#   a114_divisible.py

# get two numbers from user
var_1 = int(input("Enter a number:    "))
var_2 = int(input("Enter another number:    "))

# loop while the numbers are not divisible (the remainder is not 0)
while var_1 % var_2 != 0:

    # inform user of result
    print("your numbers are not evenly divisible")
    # gather user input again
    var_1 = int(input("Enter a number:    "))
    var_2 = int(input("Enter another number:    "))

# inform user of result
print("Your numbers are divisible")