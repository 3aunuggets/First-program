def division (num1,num2):
    if num2 == 0:
        return "You cannot divide by zero"
    divide =  num1 / num2  
    return divide  







if __name__=="__main__" :
    num1= int(input("enter a number: "))
    num2= int(input("enter a number: "))
    div = division(num1,num2)
    print("Division = ", div)