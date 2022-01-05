import json
from random import choice

words = []
with open("words.txt") as f:
    for line in f:
        words.append(line.strip())

def compare(solution, guess):
    assert(len(solution) == len(guess))
    s_list = [x for x in solution]
    g_list = [x for x in guess]
    result = [0] * len(solution)
    for i, c in enumerate(g_list):
        if s_list[i] == c:
            s_list[i] = ""
            result[i] = 2
    for i, c in enumerate(g_list):
        if result[i] == 2:
            continue
        for j, d in enumerate(s_list):
            if c == d:
                s_list[j] == ""
                result[i] = 1
    return tuple(result)

if __name__ == "__main__":
    solution = choice(words)
    win = False
    for i in range(1,7):
        guess = ""
        while True:
            inp = input("Guess a five letter word: ").strip()
            if inp in words:
                guess = inp
                break
            print("Word not in dictionary. Guess again.")
        result = compare(solution, guess)
        if result == (2,2,2,2,2):
            win = True
            print(f"You won in {i} guesses!")
            break
        print(result)

    if not win:
        print(f"You lost. Solution was {solution}.")
