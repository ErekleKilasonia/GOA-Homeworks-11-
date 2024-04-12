#Calculate BMI
def bmi(weight, height):
    x = weight / (height ** 2)
    if x <= 18.5:
        return "Underweight"
    elif x <= 25.0:
        return "Normal"
    elif x <= 30:
        return 'Overweight'
    elif x > 30:
        return "Obese"