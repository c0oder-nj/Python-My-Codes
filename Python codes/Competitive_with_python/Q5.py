import itertools 
def solve( A, B):
        mindy = 0
        ms = 0
        barry = 0
        bs = 0
        for (winner,score) in zip(A,B):
            if(winner==0):
                mindy+=1
                ms += score
            else:
                barry+=1
                bs += score
        
        if(barry>mindy):
            return bs
        else:
            global maxbs
            maxbs = 0
            for (winner,score) in zip(A,B):
                if(winner==1):
                    if(maxbs<score):
                        maxbs = score
            return ms + maxbs

print(solve([1,0,1,0,1],[18,7,14,3,27]))