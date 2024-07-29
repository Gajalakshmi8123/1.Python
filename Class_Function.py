class Multiple:
    def Subfields():
        Lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for i in Lists:
            print(i)

    def eligible():
        Gender = input("Your Gender: ")
        Age = int(input("Your Age: "))
        if Gender == 'Male' and Age >= 21:
            print("ELIGIBLE")
        elif Gender == 'Female' and Age >= 18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    
    def percentage():
        Subject1 = int(input("Enter the marks for Subject 1: "))
        Subject2 = int(input("Enter the marks for Subject 2: "))
        Subject3 = int(input("Enter the marks for Subject 3: "))
        Subject4 = int(input("Enter the marks for Subject 4: "))
        Subject5 = int(input("Enter the marks for Subject 5: "))
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        Percentage = Total / 5
        print("Total:", Total)
        print("Percentage:", Percentage)          
    
    
    def triangle1():
        Height = int(input("Enter the height of the triangle: "))
        Breadth = int(input("Enter the base of the triangle: "))
        Area_formula = (Height * Breadth) / 2
        print("Area_formula = (Height * Breadth) / 2")
        print("Area of Triangle:", Area_formula)
        
        Height1 = int(input("Enter the first side of the triangle: "))
        Height2 = int(input("Enter the second side of the triangle: "))
        Breadth = int(input("Enter the third side of the triangle: "))
        Perimeter_Triangle = Height1 + Height2 + Breadth
        print("Perimeter_Triangle = Height1 + Height2 + Breadth")
        print("Perimeter of Triangle:", Perimeter_Triangle)
    
    
    def odd_even():
        Number = int(input("Enter the number: "))
        if Number % 2 == 0:
            print(Number, "is an Even number")
        else:
            print(Number, "is an Odd number")

    def BMI():
        BMI= int(input("Enter the BMI Index:"))
        if BMI<18:
           print("UnderWeight")
        elif 18.5 <= BMI < 25:
           print("thin for height")
        elif 25 <= BMI < 30:
           print("weight")
        else:
           print("Over Weight")


    
    






