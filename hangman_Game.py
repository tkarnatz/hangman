import random



def hangman():
    word_list = ["Python", "Java", "computer", "hacker", "painter"]
    random_number = random.randint(0,4)
    word = word_list[random_number]
    wrong_guesses = 0

    stages = ["",
              "______            ",
              "|                 ",
              "|       |         ",
              "|       0         ",
              "|      /|\        ",
              "|      / \        ",
               ]

    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong_guesses < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter")
        if guess in rletters:
            character_index = rletters.index(guess)
            board[character_index] = guess
            rletters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((" ".join(board)))
        print("\n".join(stages[0: wrong_guesses + 1]))
        if "__" not in board:
              print("You win! The word was:")
              print(" ".join(board))
              win = True
              break
    if not win:
        print("\n".join(stages[: wrong_guesses]))
        print("You lose! it was {}.". format(word))

hangman()
                      
                      

    
