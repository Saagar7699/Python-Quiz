#Python quiz game

questions=('What is the Capital of India?: ',
          "Which song is India's National Anthem?:",
          "Who is the current Prime Minster of India?:",
          "In Which year did India became a Republic?: ",
          "Who was the only Governor-General of India (1948-1950)?:")
options=(("A.New Delhi","B. Mumbai","C.Bengaluru","D.Chennai"),
         ("A.Vande Matharam","B.Jana Gana Mana","C.Sare Jaha Se Acha","D.Jai Bharathi"),
         ("A.H D Devegowda","B.Rahul Gandhi","C.Nitesh Kumar","D.Narendra Modi"),
         ("A.1947","B.1952","C.1949","D.1950"),
         ("A. Pt. Jawaharlal Nehru","B.Dr. Rajendra Prasad","C.C Rajagopalachari","D.V K Menon"))

answers=("A","B","D","D","C")
gusses=[]
score=0
question_num=0

for question in questions:
    print("-"*15)
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Enter (A,B,C,D): ").upper()
    gusses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT")    
        print(f'{answers[question_num]} is the correct answer')
    question_num+=1    

print("-"*15)
print("     RESULT      ")
print("-"*15)

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()    

print("guesses: ", end=" ")
for guess in gusses:
    print(guess, end=" ")
print()   

score=int(score/len(questions)*100)
print(f'Your Score is: {score}%')