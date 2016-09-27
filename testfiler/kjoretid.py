tall = 0

def funksjon(n):
    gjorNoe(n//6)
    if (n >= 1):
        funksjon(n//3)
        funksjon(2*n//3)

def gjorNoe(n):
    tallet()
    while n > 0:
        n -= 1
def tallet():
    print(tall+1)
funksjon(100)
