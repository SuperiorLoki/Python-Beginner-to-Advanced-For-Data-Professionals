import random
from nltk.corpus import words
word_list = words.words()

wordle_words = [
    "crane", "slump", "grime", "blaze", "whirl",
    "brisk", "glove", "stare", "pound", "sneak",
    "charm", "trove", "blink", "flame", "wrist",
    "spine", "gloom", "latch", "swirl", "climb",
    "draft", "slice", "hatch", "noble", "trick",
    "hover", "plant", "sweep", "grain", "torch",
    "flick", "sting", "pride", "quilt", "scoop",
    "plume", "crisp", "tiger", "blunt", "swear",
    "drink", "flock", "spend", "boast", "gleam",
    "crush", "vivid", "choke", "snare", "pouch"
]
random_num = random.randint(0, (len(wordle_words)-1))
word = wordle_words[random_num]
used_words = []
correct_words = []

def check_guess(word, guess):
    status = []
    for i in range(5):
        if word[i] == guess[i]:
            status.append(f"{guess[i]} 🟢")
        elif guess[i] in word:
            status.append(f"{guess[i]} 🟡")
            if guess[i] not in correct_words:
                correct_words.append(guess[i])
        elif word[i] != guess[i]:
            status.append("🔴")
            if guess[i] not in used_words:
                used_words.append(guess[i])
    print(f"Used Letters: {used_words}")
    print(f"Misplaced Letters: {correct_words}")
    print(status)

#print(word)
i=0
while i < 5:
    guess = input(f"Please enter guess #{i+1}: ")
    if guess.lower() not in word_list:
        print("Please print a real world.")
        inputs = input("Is this a real world. Please be honest. If it is not, then type N. If it is, then type Y. ")
        if inputs == "Y" or "y":
            word_list.append(guess)
            print("We have fixed our system. Go ahead and try it again")
    elif len(guess) == 5:
        check_guess(word, guess)
        if word==guess:
            print("Congrats you got the word.")
            break
        i+=1
        if i == 5:
            print(f"Better luck next time. The correct word was {word}")
    elif len(guess) != 5:
        print("Must be a 5 letter word.")
    print("--------------------------------------------------------------------------------")




