import time 
import pyttsx3
import math
import random

# speak function
engine = pyttsx3.init()

# user input
name = input("Enter your name: ")

# greeting
engine.say(f"Assalamualaikum {name}")
engine.runAndWait()

# login system
for i in range(4):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == name and password == '1234':
        print("You are successfully logged in")
        engine.say("You are successfully logged in")
        engine.runAndWait()
        break
    else:
        print("Invalid username & password")
        engine.say("Invalid username and password")
        engine.runAndWait()

# time greeting
hour = int(time.strftime('%H'))

if hour < 12:
    print("Good morning", name)
    engine.say(f"Good morning {name}")
elif hour < 17:
    print("Good afternoon", name)
    engine.say(f"Good afternoon {name}")
else:
    print("Good evening", name)
    engine.say(f"Good evening {name}")
engine.runAndWait()

# menu options
options = {
    1: 'Calculator',
    2: 'Guessing number game',
    3: 'Question answers game',
    4: 'Exit'
}

while True:
    print("\nMenu Options:")
    for key, value in options.items():
        print(f"{key}. {value}")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Welcome to Adnan's Calculator")
        engine.say("Calculate your values")
        engine.runAndWait()
        
        op = input("Enter operation ['add','subtract','multiply','divide','power','modulus','average','sin','cos','tan','exit']: ").lower()
        if op == 'exit':
            print("Good bye!")
            engine.say("Exiting calculator...")
            engine.runAndWait()
            continue
        
        # if operation needs one number only
        if op in ['sin', 'cos', 'tan']:
            num = float(input("Enter your number: "))
            
            if op == 'sin':
                result = math.sin(math.radians(num))
            elif op == 'cos':
                result = math.cos(math.radians(num))
            elif op == 'tan':
                result = math.tan(math.radians(num))
        
        # if operation needs two numbers
        else:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            
            if op == 'add':
                result = num1 + num2
            elif op == 'subtract':
                result = num1 - num2
            elif op == 'multiply':
                result = num1 * num2
            elif op == 'divide':
                result = num1 / num2 if num2 != 0 else "Error! Division by zero"
            elif op == 'power':
                result = num1 ** num2
            elif op == 'modulus':
                result = num1 % num2
            elif op == 'average':
                result = (num1 + num2) / 2
            else:
                result = "Invalid operation!"
        
        print("Result:", result)
        engine.say(str(result))
        engine.runAndWait()
    
    
        # --------------- Guessing number game ---------
    elif choice == 2:
        secret = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        print("Welcome to Guessing Game,", name)
        print("I am thinking of a number between 1 and 100.")
        engine.say("Welcome to Guessing Game. I am thinking of a number between 1 and 100.")
        engine.runAndWait()
        
        while attempts < max_attempts:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations {name}! You guessed it in {attempts} tries.")
                engine.say(f"Congratulations {name}, you guessed the number correctly in {attempts} tries.")
                engine.runAndWait()
                break
        else:
            print(f"😢 Sorry {name}, you are out of attempts. The number was {secret}.")
            engine.say(f"Sorry {name}, you are out of attempts. The number was {secret}.")
            engine.runAndWait()

    # ---------------- QUIZ GAME ----------------
    elif choice == 3:
        print("Welcome to Quiz game,", name)
        print("I am asking you some questions and you answer them")
        engine.say(f"Welcome to Quiz game {name}")
        engine.runAndWait()

        questions = {
            "If y=4 and x=5 then tell z=? if z = x*y. ": "20",
            "If a=13.3 and b=32, then show that y=34, if y=a/b? ": "not equal",
            "23*2/5+6-4=? ": "11.2",
            "What is the formula of CV%? ": "s.d/mean"
        }

        score = 0
        for question, ans in questions.items():
            user_ans = input(question).lower()
            if user_ans == str(ans).lower():
                print("✅ Correct answer,", name)
                score += 1
            else:
                print("❌ Wrong answer,", name)

        print(f"\n{name}, your final score is {score}/{len(questions)}")
        engine.say(f"Your final score is {score} out of {len(questions)}")
        engine.runAndWait()
    
    # ---------------- EXIT ----------------
    elif choice == 4:
        print("Exiting program...")
        engine.say(f"Goodbye {name}")
        engine.runAndWait()
        break
    

   