def get_word():
    from random_word import RandomWords

    word = " "

    while word == " ":
        difficulty = str(input("enter the difficulty of the word you would like to guess (easy, medium, hard)")).lower()

        if difficulty == "easy":
            word = RandomWords().get_random_word(minLength = 2, maxLength = 5)
        elif difficulty == "medium":
            word = RandomWords().get_random_word(minLength = 6, maxLength = 8)
        elif difficulty == "hard":
            word = RandomWords().get_random_word(minLength = 9, maxLength = 12)
    
    return word 