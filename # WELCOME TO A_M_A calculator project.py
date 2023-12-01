# WELCOME TO M_A_A calculator project
number_1 = int (input ( "please enter your first number : "))
amaliat =input ("select between ( + , - , * , / , ^)" )
number_2 = int (input ( "please enter your second number : "))
if amaliat ==  "+": 
    resault = number_1 + number_2
    print ("here is your resault : " , resault )
elif amaliat == "-" :
    resault = number_1 - number_2
    print (" here is your resault : " , resault )
elif amaliat == "*" :
    resault = number_1 * number_2 
    print (" here is your resault : " , resault)
elif amaliat == "/" :
    if number_1 != 0 and number_2 != 0 :
        resault = number_1 / number_2 
    else :
        print ("It is not possible to divide by zero")
elif amaliat == "^" :
    resault = number_1 ** number_2 
    print (" here is your resault : " , resault)
else :
    print ( "invalid nums or amaliat")