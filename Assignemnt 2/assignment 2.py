import random
def xEuclidean(n, m):
    q,r=0,1
    w,t=1,0
    while (m!=0):
        quotient=n//m
        n,m=m,n-quotient*m
        r,q= q,r-quotient*q
        t,w=w,t-quotient*w
    return n,r,t

def chooseKeys():
    r1=random.randint(100,300)
    r2=random.randint(100,300)
    fo=open('primenumbers.txt','r')
    lines=fo.read().splitlines()
    fo.close()
    p1=int(lines[r1])
    p2=int(lines[r2])
    n=p1*p2
    l=(p1-1)*(p2-1)
    e=chose(l)
    Euclidean,q,w=xEuclidean(e,l)
    if (q<0):
        d=q+l
    else:
        d=q
    f_public = open('pub_keys.txt', 'w')
    f_public.write(str(n)+'\n')
    f_public.write(str(e)+'\n')
    f_public.close()
    f_private = open('pri_keys.txt', 'w')
    f_private.write(str(n)+'\n')
    f_private.write(str(d)+'\n')
    f_private.close()


def Euclidean(n,m):
    if (m==0):
        return n
    else:
        return Euclidean(m,n%m)
    
def chose(l):
     while (True):
        e=random.randrange(2,l)
        if (Euclidean(e,l)==1):
            return e

def encrypt(m,file_name='pub_keys.txt',block_size=2):
    try:
        fo=open(file_name, 'r')
    except FileNotFoundError:
        print('file not found.')
    else:
        n=int(fo.readline())
        e=int(fo.readline())
        fo.close()
        eb=[]
        ct=-1
        if (len(m)>0):
            ct=ord(m[0])
        for i in range(1, len(m)):
            if (i % block_size == 0):
                eb.append(ct)
                ct=0
            ct=ct*1000+ord(m[i])
        eb.append(ct)
        for i in range(len(eb)):
            eb[i]=str((eb[i]**e) % n)
        em= " ".join(eb)
        return em
    
def decrypt(blocks,block_size=2):
    fo=open('pri_keys.txt','r')
    n=int(fo.readline())
    d=int(fo.readline())
    fo.close()
    list_blocks=blocks.split(' ')
    int_blocks=[]
    for s in list_blocks:
        int_blocks.append(int(s))
    m=""
    for i in range(len(int_blocks)):
        int_blocks[i]=(int_blocks[i]**d)%n    
        tmp=""
        for c in range(block_size):
            tmp=chr(int_blocks[i]%1000)+tmp
            int_blocks[i]//=1000
        m+=tmp
    return m

def main():
    instruction = input('What you want to do encrypt or decrypt? (Enter e or d): ')
    if (instruction=='e'):
        m=input('Type the message to encrypt\n')
        chooseKeys()
        print('Encrypting please wait...')
        print(encrypt(m))  
    elif (instruction=='d'):
        m=input('Type message to decrypt?\n')
        print('Decrypting please wait...')
        print(decrypt(m))
    else:
        print('error,please type correcr instruction.')

main()
