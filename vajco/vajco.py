K = 54
P = 49
D = 4446
S = 0

def prvni_slepica(K, P, D, S):
    if (D-K)>=0:
        D-=K
        S+=1
        D-=P
        return (druha_slepica(K, P, D, S))
    else:
        return S
    
def druha_slepica(K, P, D, S):
    if (D-K)>=0:
        D-=K
        S+=1
        return (treti_slepica(K, P, D, S))
    else:
        return S
    
def treti_slepica(K, P, D, S):
    if (D-P)>=0:
        D-=P
        S+=1
        return (treti_slepica(K, P, D, S))
    else:
        return S
    
print(prvni_slepica(K, P, D, S))
