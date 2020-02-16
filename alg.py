
def confused(n_tup:tuple):
    r_tup = ()
    if len(set(n_tup)) == 1:
        return 0
    for n in n_tup:
        r_tup += (getP(n),)

    bitch = ((3+ sum(r_tup[:3]))/(1+r_tup[-1])) -1

    if bitch >2.5:
        return 100
    elif bitch >2:
        return 80
    elif bitch > 1.5:
        return 60
    elif bitch > 1:
        return 40
    elif bitch > 0.5:
        return 20
    elif bitch<=0.5:
        return 0
    else:
        return bitch*100



def getP(num:int) ->float:
        return num*0.2
