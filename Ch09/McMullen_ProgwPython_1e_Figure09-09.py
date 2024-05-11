def correct(answer_is_correct):
    if answer_is_correct:
        print("Correct!")
        print("Each correct answer is worth 1 point.")
        score += 1
    else:
        print("Not correct.")
        
score = 0
answer = input("Lake Chapala is the largest freshwater lake in which country? ")
correct(answer == "Mexico")
 
answer = input("Mac Gargan is the alter ego of what Spider-Man villain? ")
correct(answer == "Scorpion")
