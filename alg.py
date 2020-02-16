
def confused(n_tup:tuple):
    r_tup = ()
    if len(set(n_tup)) == 1:
        return 0
    for n in n_tup:
        r_tup += (getP(n),)

    thresh = ((3+ sum(r_tup[:3]))/(1+r_tup[-1])) -1
    print(thresh)
    if thresh >2.5:
        return 100
    elif thresh >2:
        return 80
    elif thresh > 1.5:
        return 60
    elif thresh > 1:
        return 40
    elif thresh > 0.5:
        return 20
    elif thresh<=0.5:
        return 0
    else:
        return thresh*100



def getP(num:int) ->float:
        return num*0.2
