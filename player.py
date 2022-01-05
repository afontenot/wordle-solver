import json

with open("solution.json") as f:
    solution = json.load(f)

print("Enter results with 0 = none, 1 = wrong location, 2 = correct.")
print("You can use either spaces or commas to separate letters, or nothing.")

count = 0
while True:
    count += 1
    print("Guess:", solution["guess"])
    if not "result" in solution:
        print(f"Last possible word in wordlist.\nFound in {count} guesses.")
        break
    result = input("Result: ")
    while "  " in result:
        result = result.replace("  ", " ")
    if len(result) == 5:
        result = ",".join(list(result))
    elif not "," in result:
        result = result.replace(" ", ",")
    elif ", " in result:
        result = result.replace(", ", ",")

    if result == "2,2,2,2,2":
        print(f"Succeeded in {count}.")
        break

    if not result in solution["result"]:
        print("Failed to find any solution. Possible responses were:")
        print(solution["result"].keys())

    solution = solution["result"][result]

