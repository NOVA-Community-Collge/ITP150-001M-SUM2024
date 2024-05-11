scores = {"mandy": 2,
          "fernando": 4,
          "jessica": 1,
          "prateek": 1}

scores.pop("mandy")

for key in scores.keys():
    print("Name, score:", key + ",", scores[key])