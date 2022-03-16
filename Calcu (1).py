
# Online Python - IDE, Editor, Compiler, Interpreter
#Calculator 
#Calculator with menu

def menu():
    print ("CALCULATOR")
    print ("Select an option: ")
    print ("******************")
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print ("4. Division")
    print ("0. Exit")
    option=input("Enter choice 1/2/3/4/0  ")
    return option
    
def main():
    while True:
        option=menu()
        if option=="1":
            print("Select the add option")
            a=int(input("Enter the first number :"))
            b=int(input("Enter the second number :"))
            print("This is the score of the addition:" + str (a+b))
            
        if option=="2":
            print("Select the subtract option")
            a=int(input("Enter the first number :"))
            b=int(input("Enter the second number :"))
            print("This is the score of the subtraction:" + str (a-b))
            
        if option=="3":
            print("Select the multiply option")
            a=int(input("Enter the first number :"))
            b=int(input("Enter the second number :"))
            print("This is the score of the multiplication:" + str (a*b))
            
        if option=="4":
            print("Select the division option")
            a=int(input("Enter the first number :"))
            b=int(input("Enter the second number :"))
            print("This is the score of the divide:" + str (a/b))
            
        elif option=="0":
            break
        
main()