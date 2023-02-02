#Encryption
import time
import random

def worker():
    dic={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    dic_new={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
    print("Enter the Text for Encryption:-",end=" ")
    encryption=input()
    print()
    print("Here is your 1st hashing Starting Automatically:- ")
    time.sleep(2)
    print()
    storer=[]
    print("Processing your Requirements")
    encryption=encryption.lower()
    storer=GP(encryption,10,dic)
    time.sleep(2)
    print()
    print("Here is your 1st level of hashing Completed:- ")
    print()
    for i,j in storer:
        time.sleep(0.5)
        print(j," :- ",i)
    print()
    print("Which Level you want for further levels:-",end=" ")
    l=int(input())
    print()
    print("Here is your 2nd hashing Starting Automatically:- ")
    print()
    level=10
    for i,j in storer:
        if j==l:
            encryption=i
            break
    storer=[]
    convert=AP(encryption,level,dic)
    storer=GP(convert,level,dic)
    k=1
    for i,j in storer:
        storer[j-1][0]=AP(i,j,dic)+str(l)+str(k)
        k+=1
    print("Processing your Requirements")
    print()
    time.sleep(2)
    print()
    print("Here is your 2nd level of hashing Completed:- ")
    print()
    for i,j in storer:
        time.sleep(0.5)
        print(j," :- ",i)
    print()
    print("Which Level of Hashing you want for further levels :-",end=" ")
    l1=int(input())
    print()
    for i,j in storer:
        if j==l1:
            level1,encryption=j,i
            break
    time.sleep(2)
    real_encryption=falsechr(encryption,l,dic_new)
    print("Here is your False character setter -",end=" ")
    print(real_encryption)
    print()
    time.sleep(2)
    print("Here is your reverse encryption text -",end=" ")
    real_encryption=real_encryption[::-1]
    print(real_encryption)
    while 1:
        time.sleep(1)
    
def converter(cr,x,dic):
    send=""
    value=dic[x]
    value+=cr
    if value>26:
        while value>26:
            value=(value-26)
    send=chr(value+96)
    return send

def GP(x,l,dic):
    storer=[]
    min_storer=[]
    c=1
    n=0
    cr=2
    dup_cr=cr
    changer=""
    while c<l:
        changer=""
        min_storer=[]
        n=0
        for i in range(0,len(x)):
            cr=(dup_cr**n)
            changer+=converter(cr,x[i],dic)
            n+=1
        min_storer.append(changer)
        min_storer.append(c)
        storer.append(min_storer)
        c+=1
        cr=dup_cr
        cr+=1
        dup_cr=cr
    return storer

def AP(x,l,dic):
    n=1
    changer=""
    for i in range(0,len(x)):
        changer+=converter(l*n,x[i],dic)
        n+=1
    return changer

def falsechr(encryption,l,dic_new):
    real_encryption=""
    a=list(i for i in range(1,27))
    counter=0
    falsechr=""
    while counter!=len(encryption):
        falsechr=""
        for i in range(1,l+1):
            falsechr+=dic_new[random.choice(a)]
        real_encryption+=falsechr+encryption[counter]
        counter+=1
        l+=1
    return real_encryption


if __name__=="__main__":
    worker()
    
    
        
    
