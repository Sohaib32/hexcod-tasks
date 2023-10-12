import random

def generate_random_number():
    return ''.join(random.sample("0123456789", 4))

def count_cows_and_bulls(secret, guess):
    cows = bulls = 0
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1
    return cows, bulls

def main():
    secret_number = generate_random_number()
    guesses = 0

    print("Welcome to the Cows and Bulls Game!")

    while True:
        user_guess = input("Enter a 4-digit number (or 'exit' to quit): ")

        if user_guess.lower() == 'exit':
            print(f"The secret number was {secret_number}. You made {guesses} guesses. Goodbye!")
            break

        if not user_guess.isdigit() or len(user_guess) != 4:
            print("Please enter a valid 4-digit number.")
            continue

        guesses += 1
        cows, bulls = count_cows_and_bulls(secret_number, user_guess)

        if cows == 4:
            print(f"Congratulations! You guessed the correct number '{secret_number}' in {guesses} guesses.")
            break
        else:
            print(f"{cows} cow(s), {bulls} bull(s)")

if __name__ == "__main__":
    main()
