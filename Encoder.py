import random
a = input("Enter message: ")
words = a.split(" ")
coding = True
if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = "dfg"
            r2 = "ert"
            anew = (r1) + word[1:] + word[0] + r2 
            nwords.append(anew)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))
    
else:
    nwords =[]
    for word in words:
        if len(word)>=3:
            anew = word[3:-3]
            anew = anew[-1] + anew[:-1]
            nwords.append(anew)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))
