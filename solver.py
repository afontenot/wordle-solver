import json

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

def getpossibles(guesses):
    possibles = []
    for word in words:
        valid = True
        for guess, result in guesses:
            if compare(word, guess) != result:
                valid = False
                break
        if valid:
            possibles.append(word)

    if len(possibles) == 0:
        print("ERROR: no possible words")
        return []

    return possibles

def getoutcomes(guess, possibles):
    outcomes = []
    for possible in possibles:
        #print("POSSIBLE:", possible)
        outcomes.append(compare(possible, guess))
    return list(set(outcomes))

def guess(possibles, printprogress=False):
    if len(possibles) == 1:
        return possibles[0]
    bestscore = 0
    bestword = ""
    # guessed word
    for i, guess in enumerate(words):
        if printprogress:
            print(f"\rSearched {i+1}/{len(words)} words", end="")
        score = 0
        # correct word
        for correct in possibles:
            res = compare(correct, guess)
            # how many possible words are eliminated
            for word in possibles:
                if compare(word, guess) != res:
                    score += 1
        if score > bestscore:
            bestscore = score
            bestword = guess
        elif score == bestscore and guess in possibles:
            bestword = guess

    return bestword

def getkeyfromtuple(tup):
    return ','.join([str(x) for x in tup])

def search(path=[]):
    # narrow down to the part of the search tree specified by `path`
    mytree = tree
    guesses = []
    for part in path:
        guesses.append((mytree["guess"], part))
        mytree = mytree["result"][getkeyfromtuple(part)]

    possibles = getpossibles(guesses)
    outcomes = getoutcomes(mytree["guess"], possibles)

    if len(outcomes) == 1 and outcomes[0] == (2,2,2,2,2):
        del mytree["result"]

    for i, outcome in enumerate(outcomes):
        if len(path) == 0:
            print(f"\nLEVEL 0: {i+1}/{len(outcomes)}")
        elif len(path) == 1:
            print(f"\rLEVEL 1: {i+1}/{len(outcomes)}", end='')
        if outcome == (2,2,2,2,2):
            continue
        mytree["result"][getkeyfromtuple(outcome)] = {"guess": None, "result": {}}
        myguesses = guesses + [(mytree["guess"], outcome)]
        mypossibles = getpossibles(myguesses)
        if len(path) == 0:
            print(f"LEVEL 0: guessing for {outcome}")
        mytree["result"][getkeyfromtuple(outcome)]["guess"] = guess(mypossibles)
        mypath = path + [outcome]
        search(mypath)

# Find the initial word (turns out to be "raise")
print("Searching for the best initial guess. May take hours to locate.")
initialword = guess(words, printprogress=True)
tree = {"guess": initialword, "result": {}}
search()

with open("solution.json", 'w') as f:
    f.write(json.dumps(tree, sort_keys=True, indent=2))
