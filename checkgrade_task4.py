#check grade
def check_grade(grade):
    if grade >= 80 and grade <=99:
        return "You got a good grade"
    elif grade >= 70 and grade <= 79:
        return "keep it up"
    elif grade >= 60 and grade <= 69:
        return "sorry your grade is too low"
    elif grade <= 59:
        return "You failed"

User_Grade = int(input("Enter your fucking grade User!:  "))    
print(check_grade(User_Grade))