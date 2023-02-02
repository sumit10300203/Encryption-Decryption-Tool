#Decryption
import time
def worker():
    dic={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    dic_new={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
    print("Enter the Text for Decryption:-",end=" ")
    decryption=input()
    decryption=decryption.lower()
    decryption=decryption[::-1]
    level=int(decryption[len(decryption)-1])
    for i in decryption:
        if i.isdigit():
            l=int(i)
            break
    decryption=decryption[0:len(decryption)-2]
    decryption=falsechr(decryption,l,dic_new)
    convert=AP(decryption,level,dic)
    storer=GP(convert,level+1,dic)
    storer=AP(storer,10,dic)
    storer=GP(storer,l+1,dic)
    print("The Decrypted Text is:-",storer)
    while 1:
        time.sleep(1)
def converter(cr,x,dic):
    send=""
    value=dic[x]
    value=value-cr
    if value<=0:
        while value<=0:
            value=(value+26)
    send=chr(value+96)
    return send
def AP(x,l,dic):
    n=1
    changer=""
    for i in range(0,len(x)):
        changer+=converter(l*n,x[i],dic)
        n+=1
    return changer
def GP(x,l,dic):
    cr=l
    dup_cr=cr
    changer=""
    n=0
    for i in range(0,len(x)):
        cr=(dup_cr**n)
        changer+=converter(cr,x[i],dic)
        n+=1
    storer=changer
    return storer
def falsechr(storer,level,dic_new):
    real_decryption=""
    counter=0
    for i in storer:
        if counter==level:
                real_decryption+=i
                counter=0
                level+=1
        else:
                counter+=1
    return real_decryption[0:len(real_decryption)-1]


if __name__=="__main__":
    worker()
