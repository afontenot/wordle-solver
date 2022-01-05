# wordle-solver: a nearly-optimal computer player for Wordle

[Wordle](https://www.powerlanguage.co.uk/wordle/) is an interesting word
guessing game. This program plays it very well, taking only 3.68 guesses on
average and never more than 5.

 * words.txt - contains every word that Wordle uses as a possible solution, as
of Jan 2021.
 * solver.py - solves the game optimally (subject to several constraints)

You probably only want to use player.py: it will use a pre-generated solution
stored in solution.json to play the game for you.

If you want to play Wordle more than once a day, you can use game.py to
generate endless games.
