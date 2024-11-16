# if-else + loops
numbers = [-2, -4, -5, 6, 7, 8, 0, 0,]
for num in numbers:
    if num > 0:
        print(f"the {num} is negative")
    elif num < 0:
        print(f"the {num} is positive")
    else:
        print(f"the {num} is zero")        
# if-else + while
target_number = 7
guess = None

while guess != target_number:
    number = int(input("Guess a number between 1 and 10: "))
    
    if number < target_number:
        print("Too low! Try again.")
    elif number > target_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number.")