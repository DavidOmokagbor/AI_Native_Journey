#!/usr/bin/env python3
"""
🎓 INTERACTIVE PYTHON LEARNING TOOL 🎓
A comprehensive tutorial covering all concepts learned in the last 5 days!
"""

import time
import random

def print_slow(text, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_header(title):
    """Print a beautiful header"""
    print("\n" + "="*60)
    print(f"🎯 {title}")
    print("="*60)

def print_success():
    """Print a success message"""
    print("\n✅ Great job! You've completed this section!")
    print("="*60)

def wait_for_enter():
    """Wait for user to press Enter"""
    input("\nPress Enter to continue...")

def lesson_1_variables_and_print():
    """Lesson 1: Variables and Print Statements"""
    print_header("LESSON 1: VARIABLES & PRINT STATEMENTS")
    
    print_slow("Welcome to your Python journey! Let's start with the basics.")
    print_slow("\nVariables are like containers that store information.")
    print_slow("Think of them as labeled boxes where you can put things!")
    
    wait_for_enter()
    
    print_slow("\nLet's create some variables together:")
    print_slow("name = 'Python Learner'")
    print_slow("age = 25")
    print_slow("favorite_color = 'blue'")
    
    wait_for_enter()
    
    print_slow("\nNow let's print them using different methods:")
    print_slow("print('Hello, ' + name)  # String concatenation")
    print_slow("print(f'You are {age} years old')  # f-strings (modern way)")
    print_slow("print('Your favorite color is', favorite_color)  # Multiple values")
    
    wait_for_enter()
    
    # Interactive exercise
    print_slow("\n🎯 YOUR TURN: Let's practice!")
    user_name = input("What's your name? ")
    user_age = input("How old are you? ")
    user_color = input("What's your favorite color? ")
    
    print_slow(f"\nPerfect! Let's print your information:")
    print(f"Hello, {user_name}!")
    print(f"You are {user_age} years old")
    print(f"Your favorite color is {user_color}")
    
    print_success()

def lesson_2_input_and_interaction():
    """Lesson 2: Input and User Interaction"""
    print_header("LESSON 2: INPUT & USER INTERACTION")
    
    print_slow("Now let's learn how to get information from users!")
    print_slow("The input() function lets us ask questions and get answers.")
    
    wait_for_enter()
    
    print_slow("\nExample:")
    print_slow("user_name = input('What is your name? ')")
    print_slow("print(f'Hello, {user_name}!')")
    
    wait_for_enter()
    
    # Interactive exercise
    print_slow("\n🎯 YOUR TURN: Let's build a simple calculator!")
    
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    
    # Convert to integers
    num1 = int(num1)
    num2 = int(num2)
    
    print_slow(f"\nResults:")
    print(f"Addition: {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} × {num2} = {num1 * num2}")
    print(f"Division: {num1} ÷ {num2} = {num1 / num2}")
    
    print_success()

def lesson_3_control_flow():
    """Lesson 3: Control Flow (if/else statements)"""
    print_header("LESSON 3: CONTROL FLOW (IF/ELSE STATEMENTS)")
    
    print_slow("Control flow lets your program make decisions!")
    print_slow("It's like giving your computer a brain to choose what to do.")
    
    wait_for_enter()
    
    print_slow("\nBasic if/else structure:")
    print_slow("if condition:")
    print_slow("    # do this if condition is True")
    print_slow("else:")
    print_slow("    # do this if condition is False")
    
    wait_for_enter()
    
    # Interactive weather example
    print_slow("\n🎯 YOUR TURN: Weather-based coffee recommendation!")
    
    temperature = input("What's the temperature outside? (Enter a number): ")
    temperature = int(temperature)
    
    if temperature > 25:
        print("☀️ It's warm! Let's make an iced coffee! 🧊")
    elif temperature > 15:
        print("🌤️ Nice weather! A regular coffee sounds good! ☕")
    else:
        print("❄️ It's chilly! Let's make a hot coffee! 🔥")
    
    wait_for_enter()
    
    # Interactive age checker
    print_slow("\n🎯 YOUR TURN: Age-based movie recommendation!")
    
    age = input("How old are you? ")
    age = int(age)
    
    if age >= 18:
        print("🎬 You can watch R-rated movies!")
    elif age >= 13:
        print("🎬 You can watch PG-13 movies!")
    else:
        print("🎬 You can watch G and PG movies!")
    
    print_success()

def lesson_4_functions():
    """Lesson 4: Functions"""
    print_header("LESSON 4: FUNCTIONS")
    
    print_slow("Functions are like recipes - they package code into reusable blocks!")
    print_slow("They help you organize your code and avoid repetition.")
    
    wait_for_enter()
    
    print_slow("\nFunction structure:")
    print_slow("def function_name(parameters):")
    print_slow("    # function code here")
    print_slow("    return result")
    
    wait_for_enter()
    
    # Interactive function creation
    print_slow("\n🎯 YOUR TURN: Let's create a function together!")
    
    def greet_person(name, time_of_day="day"):
        """A function that greets someone"""
        if time_of_day == "morning":
            return f"Good morning, {name}! ☀️"
        elif time_of_day == "evening":
            return f"Good evening, {name}! 🌙"
        else:
            return f"Hello, {name}! 👋"
    
    print_slow("We just created a function called 'greet_person'!")
    
    # Test the function
    user_name = input("\nWhat's your name? ")
    time_pref = input("What time is it? (morning/evening/day): ")
    
    greeting = greet_person(user_name, time_pref)
    print(f"\n{greeting}")
    
    print_success()

def lesson_5_loops():
    """Lesson 5: Loops"""
    print_header("LESSON 5: LOOPS")
    
    print_slow("Loops let you repeat actions without writing the same code over and over!")
    print_slow("They're like telling your computer: 'Do this until I say stop!'")
    
    wait_for_enter()
    
    print_slow("\nTwo main types of loops:")
    print_slow("1. for loops - when you know how many times to repeat")
    print_slow("2. while loops - when you want to repeat until a condition is met")
    
    wait_for_enter()
    
    # Interactive for loop
    print_slow("\n🎯 YOUR TURN: Let's count with a for loop!")
    
    count_to = input("Count to what number? ")
    count_to = int(count_to)
    
    print_slow("Counting...")
    for i in range(1, count_to + 1):
        print(f"Number {i}!")
        time.sleep(0.5)
    
    wait_for_enter()
    
    # Interactive while loop
    print_slow("\n🎯 YOUR TURN: Let's play a guessing game!")
    
    secret_number = random.randint(1, 10)
    attempts = 0
    
    print_slow("I'm thinking of a number between 1 and 10...")
    
    while True:
        guess = input("Your guess: ")
        guess = int(guess)
        attempts += 1
        
        if guess == secret_number:
            print(f"🎉 Correct! You got it in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("📈 Too low! Try again.")
        else:
            print("📉 Too high! Try again.")
    
    print_success()

def lesson_6_lists_and_data_structures():
    """Lesson 6: Lists and Data Structures"""
    print_header("LESSON 6: LISTS & DATA STRUCTURES")
    
    print_slow("Lists are like shopping lists - they hold multiple items!")
    print_slow("They're perfect for storing collections of data.")
    
    wait_for_enter()
    
    print_slow("\nCreating and using lists:")
    print_slow("fruits = ['apple', 'banana', 'orange']")
    print_slow("print(fruits[0])  # prints 'apple' (first item)")
    print_slow("fruits.append('grape')  # adds 'grape' to the list")
    
    wait_for_enter()
    
    # Interactive list exercise
    print_slow("\n🎯 YOUR TURN: Let's create your favorite things list!")
    
    favorites = []
    
    print_slow("Let's add your favorite things to a list:")
    for i in range(3):
        item = input(f"Favorite thing #{i+1}: ")
        favorites.append(item)
    
    print_slow(f"\nYour favorites list: {favorites}")
    print_slow(f"First favorite: {favorites[0]}")
    print_slow(f"Last favorite: {favorites[-1]}")
    print_slow(f"Number of favorites: {len(favorites)}")
    
    print_success()

def lesson_7_error_handling():
    """Lesson 7: Error Handling"""
    print_header("LESSON 7: ERROR HANDLING")
    
    print_slow("Sometimes things go wrong in programs - that's normal!")
    print_slow("Error handling helps your program deal with problems gracefully.")
    
    wait_for_enter()
    
    print_slow("\nTry/except structure:")
    print_slow("try:")
    print_slow("    # code that might cause an error")
    print_slow("except:")
    print_slow("    # what to do if there's an error")
    
    wait_for_enter()
    
    # Interactive error handling
    print_slow("\n🎯 YOUR TURN: Let's handle some errors!")
    
    while True:
        try:
            number = input("Enter a number: ")
            number = int(number)
            print(f"Great! You entered: {number}")
            break
        except ValueError:
            print("❌ That's not a valid number! Try again.")
    
    print_success()

def final_project():
    """Final Project: Putting it all together"""
    print_header("FINAL PROJECT: PERSONAL ASSISTANT")
    
    print_slow("🎉 Congratulations! You've learned so much!")
    print_slow("Now let's build something amazing using everything you've learned!")
    
    wait_for_enter()
    
    print_slow("\nLet's create a personal assistant that can:")
    print_slow("• Remember your name")
    print_slow("• Calculate things")
    print_slow("• Give weather-based advice")
    print_slow("• Play games")
    print_slow("• Store your favorite things")
    
    wait_for_enter()
    
    # Get user info
    name = input("What's your name? ")
    age = input("How old are you? ")
    
    # Store favorites
    favorites = []
    print_slow("\nLet's add some of your favorite things:")
    for i in range(3):
        item = input(f"Favorite #{i+1}: ")
        favorites.append(item)
    
    # Main assistant loop
    print_slow(f"\n🤖 Hello {name}! I'm your personal assistant!")
    
    while True:
        print_slow("\nWhat would you like me to do?")
        print("1. Calculate something")
        print("2. Give weather advice")
        print("3. Play a number game")
        print("4. Show your favorites")
        print("5. Exit")
        
        choice = input("\nYour choice (1-5): ")
        
        if choice == "1":
            # Calculator
            try:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))
                operation = input("Operation (+, -, *, /): ")
                
                if operation == "+":
                    result = num1 + num2
                elif operation == "-":
                    result = num1 - num2
                elif operation == "*":
                    result = num1 * num2
                elif operation == "/":
                    result = num1 / num2
                else:
                    print("❌ Invalid operation!")
                    continue
                
                print(f"Result: {num1} {operation} {num2} = {result}")
            except ValueError:
                print("❌ Please enter valid numbers!")
        
        elif choice == "2":
            # Weather advice
            try:
                temp = int(input("What's the temperature? "))
                if temp > 25:
                    print("☀️ Hot day! Stay hydrated and wear sunscreen!")
                elif temp > 15:
                    print("🌤️ Nice weather! Perfect for outdoor activities!")
                else:
                    print("❄️ Cold day! Bundle up and stay warm!")
            except ValueError:
                print("❌ Please enter a valid temperature!")
        
        elif choice == "3":
            # Number game
            secret = random.randint(1, 20)
            attempts = 0
            print_slow("I'm thinking of a number between 1 and 20...")
            
            while True:
                try:
                    guess = int(input("Your guess: "))
                    attempts += 1
                    
                    if guess == secret:
                        print(f"🎉 Correct! You got it in {attempts} attempts!")
                        break
                    elif guess < secret:
                        print("📈 Too low!")
                    else:
                        print("📉 Too high!")
                except ValueError:
                    print("❌ Please enter a valid number!")
        
        elif choice == "4":
            # Show favorites
            print_slow(f"\nYour favorite things:")
            for i, item in enumerate(favorites, 1):
                print(f"{i}. {item}")
        
        elif choice == "5":
            print_slow(f"\n👋 Goodbye {name}! Thanks for using your personal assistant!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-5.")
        
        wait_for_enter()

def main():
    """Main function to run the learning tool"""
    print_header("🎓 WELCOME TO THE INTERACTIVE PYTHON LEARNING TOOL! 🎓")
    
    print_slow("This tool will teach you everything you need to know about Python!")
    print_slow("Each lesson builds on the previous one, so follow along carefully.")
    
    wait_for_enter()
    
    # Run all lessons
    lesson_1_variables_and_print()
    lesson_2_input_and_interaction()
    lesson_3_control_flow()
    lesson_4_functions()
    lesson_5_loops()
    lesson_6_lists_and_data_structures()
    lesson_7_error_handling()
    
    print_header("🎉 CONGRATULATIONS!")
    print_slow("You've completed all the lessons!")
    print_slow("Now let's build something amazing with everything you've learned!")
    
    wait_for_enter()
    
    final_project()
    
    print_header("🏆 YOU'RE A PYTHON DEVELOPER NOW!")
    print_slow("You've learned:")
    print_slow("✅ Variables and print statements")
    print_slow("✅ User input and interaction")
    print_slow("✅ Control flow (if/else)")
    print_slow("✅ Functions")
    print_slow("✅ Loops (for and while)")
    print_slow("✅ Lists and data structures")
    print_slow("✅ Error handling")
    print_slow("✅ Building complete programs!")
    
    print_slow("\n🚀 Keep practicing and building amazing things!")
    print_slow("The world of programming is now yours to explore!")

if __name__ == "__main__":
    main()
