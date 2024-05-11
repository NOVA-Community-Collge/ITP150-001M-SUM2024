def correct(answer_is_correct):
    if answer_is_correct:
        print("Correct!")
        print("Each correct answer is worth 1 point.")
    else:
        print("Not correct.")
        
score = 0
answer = input("Lake Chapala is the largest freshwater lake in which country? ")
is_correct = answer == "Mexico"
correct(is_correct)
if is_correct:
    score += 1
 
answer = input("Mac Gargan is the alter ego of what Spider-Man villain? ")
is_correct = answer == "Scorpion"
correct(is_correct)
if is_correct:
    score += 1
