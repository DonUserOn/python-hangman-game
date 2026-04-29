import random

words = (
    "apple", "orange", "banana", "coconut", "pineapple",
    "grape", "mango", "peach", "cherry", "strawberry",
    "watermelon", "lemon", "lime", "kiwi", "papaya",
    "apricot", "blueberry", "blackberry", "raspberry", "melon",
    "carrot", "potato", "tomato", "onion", "garlic",
    "pepper", "cucumber", "lettuce", "broccoli", "cabbage",
    "school", "teacher", "student", "lesson", "pencil",
    "notebook", "computer", "keyboard", "mouse", "screen",
    "python", "program", "coding", "function", "variable",
    "internet", "website", "window", "button", "system",
    "planet", "earth", "moon", "sun", "star",
    "galaxy", "rocket", "space", "cloud", "rain",
    "river", "mountain", "forest", "desert", "ocean",
    "animal", "tiger", "lion", "monkey", "rabbit",
    "elephant", "giraffe", "zebra", "panda", "kangaroo",
    "music", "guitar", "piano", "drum", "violin",
    "movie", "camera", "picture", "artist", "painting",
    "football", "basketball", "tennis", "swimming", "running",
    "happy", "strong", "clever", "brave", "friendly",
    "travel", "airport", "ticket", "hotel", "country"
)

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

def display_man(wrong_guesses):
    print("******************************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("******************************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("The answer was:", " ".join(answer))

def main():
    answer = random.choice(words).lower()
    hint = ["_"] * len(answer)

    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Win!")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose!")
            is_running = False

if __name__ == "__main__":
    main()