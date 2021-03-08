print ("::: EASY GRADES :::")

score = 1
def computegrade (score):
    #INPUT SCORE
    score = input ("Enter score: ")
    try:
        score = float(score)
    except:
        score = -1 
        print ("Try input numbers")
        exit(score)
    #RETURN SCORE
    if 0 <= score <= 1:
            if score >= 0.9:
                a = "A"
                return(a)
            elif score >= 0.8:
                b = "B"
                return (b)
            elif score >= 0.7:
                c = "C"
                return (c)
            elif score >= 0.6:
                d = "D"
                return (d)
            elif score < 0.6:
                f = "F"
                return (F)
    else:
        print ("Score is out of range, try again")

grade = computegrade(score)
print ("Grade:", grade)
    