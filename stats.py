from collections import defaultdict
import json

words = []
with open("words.txt") as f:
    for line in f:
        words.append(line.strip())

with open("solution.json") as f:
    solution = json.load(f)

distances = []
hist = defaultdict(int)
longestdistance = 0

def find(word, tree=solution, depth=1):
    if tree["guess"] == word:
        return depth
    if "result" in tree:
        for result in tree["result"]:
            newtree = tree["result"][result]
            dep = find(word, newtree, depth+1)
            if dep != None:
                return dep
    return None

for word in words:
    distance = find(word)
    distances.append(distance)
    hist[distance] += 1
    if distance > longestdistance:
        longestdistance = distance

print("Average:", sum(distances) / len(distances))
print("Worst:", longestdistance)
for i in sorted(hist.keys()):
    print(f"{i}: {hist[i]} ({round(100*hist[i]/len(words), 1)}%)")

