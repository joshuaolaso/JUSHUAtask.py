#check aage
def check_age(age):
    if age > 25 and age < 38:
        return " Your are Adult"
    elif age > 18 and age < 25:
        return "You are Young"
    elif age > 13 and age < 17:
        return "Your arebTeenage"
    elif age > 1 and age < 12:
        return " Your are minor"

User_Age = int(input("Enter your age User?  "))    
print(check_age(User_Age))
