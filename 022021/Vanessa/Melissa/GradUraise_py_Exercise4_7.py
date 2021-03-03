def computescore(sval):
    if sval < 0:
        print('Bad score')
    elif sval > 1:
        print('Bad score')
    elif sval >= 0.9:
        print('A')
    elif sval >= 0.8:
        print('B')
    elif sval >= 0.7:
        print('C')
    elif sval >= 0.6:
        print('D')
    elif sval < 0.6 and sval > 0:
        print ('F')
    else:
        print('Bad Score')

score = input('Enter score in form 0.##: ')

try:
    sval = float(score)
except:
    sval = -1

computescore(sval)
print()
