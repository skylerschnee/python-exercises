def calculate_tip(x): 
    return float(x) * float(input("What is the bill total? "))

def get_letter_grade(n): #define the function and allow a number input
    if n >= 90:          # if the number is greater than 90:
        return 'A'       # give me this grade
    elif n >= 80:          # if the number is greater than 80:
        return 'B'       # give me this grade
    elif n >= 75:          # if the number is greater than 75:
        return 'C'       # give me this grade
    elif n >= 70:          # if the number is greater than 70:
        return 'D'       # give me this grade
    else:                # if non of the other conditions are met:
        return 'F'       # give me this grade
        
