from wordfreq import top_n_list
words = top_n_list("en", 100000)  # up to a hundred thousand most common words

# filter out words that are not 5 letters long
words = [word for word in words if len(word) == 5]

#print("Number of 5-letter words:", len(words))
#pick random word from the list
import random
word = random.choice(words)
#word = "crane"  # for testing purposes
#print("Random 5-letter word:", word)

#setup board
wordsGuessed = []
maxGuesses = 6

def printBoard():
    for guess in wordsGuessed:
        display = ""
        for i in range(5):
            if guess[i] == word[i]:
                display += "🟩"  # correct letter and position
            elif guess[i] in word:
                display += "🟨"  # correct letter but wrong position
            else:
                display += "⬜"  # incorrect letter
        print(display)
    for _ in range(maxGuesses - len(wordsGuessed)):
        print("⬜⬜⬜⬜⬜")  # empty rows for remaining guesses
    
    print("Your previous guesses:", wordsGuessed)


while len(wordsGuessed) < maxGuesses:
    printBoard()
    guess = input("Enter your 5-letter guess: ").lower()
    if guess == "restart":
        wordsGuessed = []
        word = random.choice(words)
        print("Game restarted!")
        continue
    if len(guess) != 5 or guess not in words:
        print("Invalid guess. Please enter a valid 5-letter word.")
        continue
    wordsGuessed.append(guess)
    if guess == word:
        printBoard()
        print("Congratulations! You've guessed the word:", word)
        break