def correct(user_guess, correct_answer):
    if user_guess == correct_answer:
        print("Correct!")
        print("Each correct answer is worth 1 point.")
        return 1
    else:
        print("Not correct.")
        print("The correct answer was", correct_answer + ".")
        return 0
    
score = 0
answer = input("Lake Chapala is the largest freshwater lake in which country? ")
score += correct(answer, "Mexico")
 
answer = input("Mac Gargan is the alter ego of what Spider-Man villain? ")
score += correct(answer, "Scorpion")

print("Final score:", score)