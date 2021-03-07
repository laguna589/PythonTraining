print ("..Calculator..")
hours = input("Enter hours: ")
exc = 1
try : 
    hours = float(hours)
except : 
    exc = -1
    #print("Not a number")

rate = input ("Enter rate: ")
try :
    rate = float(rate)
except :
    exc = -1
    #print("Not a number")

if exc < 0 :
    print("\nTry again, INPUT JUST NUMBERS!!")
else : 
    if hours > 40 :
        xT = hours - 40 #extra time
        xPay = rate * 0.5 * xT #payment of the extra time
        tPay = (hours * rate) + xPay #total payment
        print("Pay:", tPay)
    else :
        tPay = hours * rate #regular payment
        print("Pay:", tPay)





