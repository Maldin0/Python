"""BMI"""
def bmi():
    """Get and Print variables"""
    name = input()
    weight = float(input())
    height = float(input())/100
    bmi1 = (float(weight)/(height*height))
    print("%s's  BMI = %.2f" %(name, bmi1))
def main():
    """_"""
    bmi()
    bmi()
    bmi()
    bmi()
    bmi()
main()
