try:
    fname = input("Please, enter a file name: ")
    scores = []

    with open(fname, "r") as file:
        for i in file:
            if i.startswith("X-DSPAM-Confidence:"):
                spam_score = float(i.split(":")[1])
                scores.append(spam_score)

except FileNotFoundError:
    print("File does not exist.")
    exit()

if not scores:
    print("No emails found!")
    exit()

average_score = sum(scores) / len(scores)

print(f"Average spam confidence: {average_score}")