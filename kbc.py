print("Kaun Banega Crorepati")
ques = ["Is string a mutable data type?", "Are you learning python?"]
answers = ["no", "yes"]  # Correct answers
i = 0

for question in ques:  # Fixed: proper for loop syntax
    print(question)
    r = input("Enter your answer: ")  # Fixed: removed print() wrapper
    
    if r.lower() == answers[i].lower():  # Check against correct answer
        print(f"Correct! You won {(i+1) * 1000} rupees!")
    else:
        print(f"Wrong answer! You lost {1000} rupees!")
    
    i += 1  # Move to next question