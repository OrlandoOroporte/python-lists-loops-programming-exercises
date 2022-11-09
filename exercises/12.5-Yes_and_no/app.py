theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def textValor(x):
    if x == 1: 
        return 'wiki'
    elif x == 0:
        return 'woko'

newlist = list(map(textValor,theBools))

print(newlist)



