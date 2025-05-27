import random 
print("Hi! welcome to the Number Guessing Game.\nYou have 5 chances to guess the number. let's start!") 

low = int(input("Enter the lower Bound: ")) 
high = int(input("Enter thr higher Bound: ")) 

print(f"\n you have 5 chances to guess the number between {low} and {high}. let's start!") 

num = random.randint(low,high) 
ch = 5  # total allowed chances 
gc = 0  # guess counter 

while gc < ch: 
    gc += 1 
    guess = int(input('Enter you guess: ')) 

    if guess == num: 
        print(f'correct! the number is{num}. you guessed it in {gc} attempt.')
        break  

    elif gc >= ch and guess != num: 
        print(f'orry! the number was {num}. better luck next time.') 

    elif guess > num: 
        print('Too high! Try a lower number.')     

    elif guess < num: 
        print('Too low! Try a higher number.')      