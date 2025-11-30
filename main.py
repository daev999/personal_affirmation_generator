import random
from art import logo

# Lists of affirmations
affirmations = {
    "happy": ["I am grateful for today.", "Joy fills my heart."],
    "sad": ["I am allowed to feel.", "This too shall pass."],
    "angry": ["I choose clarity over reaction. I breathe, I think, and I stay in control.",
              "My peace matters more than anything that upset me. I let the tension go and keep my power with me."],
    "money": ["I am wise with my money. I attract abundance and manage it with clarity.",
              "I trust that God provides all I need, and I make smart choices with what I have."],
    "faith": ["God guides my steps, and I trust His timing in every area of my life.",
              "I am strengthened by faith; His peace fills me and directs my decisions."],
}

def pick_affirmation(mood):
    """Return a random affirmation based on the user's mood."""
    return random.choice(affirmations[mood])

def positivity():
    print(logo)
    print("Choose your current mood from the list below:\n")

    for key in affirmations.keys():
        print(f"- {key}")

    mood_is_valid = False
    user_mood = ""   # <-- FIX: define the variable before the loop

    # --- FIRST mood selection loop ---
    while not mood_is_valid:
        user_mood = input("\nType your mood exactly as shown: ").lower()
        if user_mood in affirmations:
            print("\nYour affirmation:")
            print(pick_affirmation(user_mood))
            mood_is_valid = True
        else:
            print("Invalid mood. Please try again.")

    # --- SECOND loop: asking for more affirmations ---
    continue_program = True

    while continue_program:
        ask_user = input("\nDo you want another affirmation? (yes/no): ").lower()

        if ask_user == "yes":
            print("\nChoose an option:")
            print("1. Another affirmation from the same mood")
            print("2. Choose a new mood")

            choice = input("Your choice (1 or 2): ")

            if choice == "1":
                print("\nYour affirmation:")
                print(pick_affirmation(user_mood))

            elif choice == "2":
                # Repeat mood selection
                new_mood_valid = False

                while not new_mood_valid:
                    new_mood = input("Enter a new mood: ").lower()
                    if new_mood in affirmations:
                        user_mood = new_mood    # update the mood
                        print("\nYour affirmation:")
                        print(pick_affirmation(user_mood))
                        new_mood_valid = True
                    else:
                        print("Invalid mood. Try again.")
            else:
                print("Invalid selection. Choose 1 or 2.")

        elif ask_user == "no":
            continue_program = False
            print("\nEvery goodbye is like a sunset, promising a sunrise. I wish you all the best on your journey.")
        else:
            print("Please answer 'yes' or 'no'.")

positivity()
