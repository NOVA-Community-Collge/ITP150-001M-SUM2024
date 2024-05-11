scores = {"mandy": 2,
          "fernando": 4,
          "jessica": 1,
          "prateek": 1}

name = input("Enter your name: ")
score = int(input("Enter your score: "))

scores[name] = score

for key in scores.keys():
    print("Name, score:", key + ",", scores[key])