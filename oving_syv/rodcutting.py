

def memo_rod_cut(p, n):
    memo = [0]*(n+1)
    for i in range(n+1):
        memo[i] = float('-inf')
    print(memo)
    return memo_rod_cut_aux(p, n, memo)

def memo_rod_cut_aux(p,n,r):
    if (r[n] >= 0):
        #print("lol")
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(n):
            verdi = p[i] + memo_rod_cut_aux(p,(n-i),r)
            if q < verdi:
                q = verdi
    r[n] = q
    print(r)
    return q

def bottom_up_cut_rod(p,n):
    r = []
    for x in range(n+1):
        r.append(x)
    r[0] = 0
    for j in range(1, n):
        q = float("-inf")
        for i in range(1, j+1):
            #print(i)
            varins = p[i] + r[j-i]
            print(varins)
            if q < varins:
                q = varins
        r[j] = q
        print(r)
    return r[n]

def main():
    p = [4,9,15,18,21,28,31,37]
    print(memo_rod_cut(p,4))
main()
