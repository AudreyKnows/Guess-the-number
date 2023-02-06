import random
import time
print("Welcome to Audrey's guessing game! I will start off by guessing a number between 1-100.")
time.sleep(3)
print("Hold on... Picking a good number")
time.sleep(2)
print("Alright, got me a good one")

guess = int(input("Guess the number?: "))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
  time.sleep(1)
  guess_count += 1
  if guess < correct_number:
    guess = int(input(" That's a bit Low dear...Guess Higher: "))

  else:
    guess = int(input("Try again, this time a bit Lower!: "))
                
print(f"Congratulations! you got the right answer, which was {correct_number}:) It only took you {guess_count} guesses!")



  
  

