









def space():
   print ("H")
   print ("T")

def space(flips, n):
    space(flips + "H", n-1)
    space(flips + "T", n-1)


def space(flips, n):
    
    if (n == 0):
        print (flips)
        return
    space(flips + "H", n-1)
    space(flips + "T", n-1)
    

import random
def toss(n):
    
    heads = 0
    tails = 0
    
    for i in range(n):
        flip = random.randint(1, n)
        if flip == 1:
           heads = heads + 1
        else:
           tails = tails + 1
    EQ1 = heads/sp
    EQ2 = tails/sp
    print('heads occurs',heads)
    print('tails occurs',tails)
    print ('Probability of Heads:', EQ1)
    print ('Probabilty of Tails:', EQ2)

if __name__=='__main__':
    
    n = int(input()) 
    sp = pow(2,n)
    print('# of sample space:',sp)
    space("", n)
    toss(n)
    



