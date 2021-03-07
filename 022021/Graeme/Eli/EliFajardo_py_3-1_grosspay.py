print ("..Calculator gross pay..")
hours = input("Enter hours: ")
rate = input ("Enter rate: ")
hours = float(hours)
rate = float(rate)
if hours > 40 :
    xT = hours - 40 #extra time
    xPay = rate * 0.5 * xT #payment of the extra time
    tPay = (hours * rate) + xPay #total payment
    print("Pay:", tPay)
else :
    tPay = hours * rate #regular payment
    print("Pay:", tPay)





