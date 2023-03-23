import random
def genNumber(n,fileName=None):
    f=open(fileName,"w")
    f.write(str(n)+"\n")
    for i in range(n):
        a=random.randrange(0,n,1)
        f.write(str(a)+"\n")
    f.close()
genNumber(6,"random")