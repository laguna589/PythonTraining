print ("::: EASY GRADES :::")
score = input ("Enter score: ")
try:
    score = float(score)
except:
    score = -1 
    print ("Try input numbers")
    exit(score)

if score >= 0 and score <= 1:
        if score >= 0.9:
            print ("A")
        elif score >= 0.8:
            print ("B")
        elif score >= 0.7:
            print ("C")
        elif score >= 0.6:
            print ("D")
        elif score < 0.6:
            print ("F")
else:
    print ("Score is out of range, try again")

    