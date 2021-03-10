#!/usr/bin/env python3

str = 'X-DSPAM-Confidence: 0.8475'

sppos = str.find(':')

num = 0.0

if (sppos > -1) :
    try :
        num = float(str[sppos + 1:].strip())
    except:
        num = None
        print('Invalid float number')

if (num is not None) :
    print(num)

