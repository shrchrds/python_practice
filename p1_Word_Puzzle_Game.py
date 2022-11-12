# Problem Statement:
# You have to write a Word Puzzle Game in which the user has to form the correct word out of a given set of characters.
# In the game the user has to solve this puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
# in random sequence. Give the user score +1 for each correct answer and give -1 for each wrong answer. At last print the final score.
# You can store any number of words in the list, but in each round of the game only 5 words are shown to the user.


def puzzle_game():
    score = 0
    problem_words = ['ETRCA', "ALUIJ", "VAAJ", "GEOLOG", "PEAPL", "LACAS", "KSFAL", "YPNTOH"]
    answers = ["REACT", "JULIA", "JAVA", "GOOGLE", "APPLE", "SCALA", "FLASK", "PYTHON"]
    solution = dict(zip(problem_words, answers))

    for i, ele in enumerate(set(solution)):
        if i == 5:
            break
        print(f"Arrange the letters to form a valid word:\n{ele}")
        ans = input("Enter your Valid word here: ").upper()

        for k,v in solution.items():
            if k == ele:
                if ans == v:
                    score = score + 1
                else:
                    score = score - 1
    print(f"Your final Score is: {score}")


puzzle_game()

