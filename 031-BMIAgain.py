"""BMI but upgraded"""
def main():
    """Calculate BMI"""
    wei = float(input())
    hei = float(input())/100
    bmi = wei/(hei*hei)
    if bmi < 18.5:
        result = "Underweight"
    elif 18.5 <= bmi < 25:
        result = "Normal"
    elif 25 <= bmi < 30:
        result = "Overweight"
    elif bmi >= 30:
        result = "Obese"
    print(result)
main()
