from time import time
cvf=0
Portal=2
import os
import binascii

zzaax=""
szxzzzas=""
asaaq=""
assa=0
adwll1=0
ddf=0
cvz31=0
rw=0
qqw1q=""
lenfzzz=0
fffgjv=""
fffgjv1=""
zzaax1=""
qqqs=0
a=0
blockw=5
blockw1=4
cvb=0
aqw1=0
zsaqq=""
qqqwz=0
assx=0
ass=0
asss=0
b=0
aaqw=""
aaqws=""
l=""
j=0
b=0
aq=0
qfl=0
t=0
h=0
byteb=""
notexist=""
lenf=0
numberschangenotexistq = []
numberschangenotexistqz = []
qwa=0
add=0
m = []
p=0
namea=""
d=1
a=0
asd=""
b=0
szx=""
asf2="0b"
while b<1790:
    m+=[-1]
    b=b+1
k = []
wer=""
qtqweqw=""
numberschangenotexist = []
numbers = []
namez = input("ul,c2 or for compress cl for extract for u2? ")
#@Author Jurijus pacalovas
class compression:

    def Areacu2(self):
                    if namez=="u2":
                        x=0
                        x1=0
                        x2=0
                        x = time()
                        name = input("What is name of file? ")
                        namea="file.W"
                        namem=""
                        namema="?"
                       
                        blockw=5
                        blockw1=4
                        nameas=name
                        nac=len(nameas)
                        if nameas[nac-8:nac]==".bin.bin":
                            nameas=nameas[0:nac-8]
                        countraz=0
                        
                        s=""
                        assx=0
                        zzaax=""
                        szxzzzas=""
                        asaaq=""
                        assa=0
                        adwll1=0
                        ddf=0
                        cvz31=0
                        rw=0
                        qqw1q=""
                        lenfzzz=0
                        fffgjv=""
                        fffgjv1=""
                        zzaax1=""
                        qqqs=0
                        a=0
                        blockw=5
                        blockw1=4
                        cvb=0
                        aqw1=0
                        zsaqq=""
                        qqqwz=0
                        assx=0
                        ass=0
                        asss=0
                        b=0
                        aaqw=""
                        aaqws=""
                        l=""
                        j=0
                        b=0
                        aq=0
                        qfl=0
                        t=0
                        h=0
                        byteb=""
                        notexist=""
                        lenf=0
                        numberschangenotexistq = []
                        numberschangenotexistqz = []
                        qwa=0
                        add=0
                        m = []
                        p=0
                        namea=""
                        d=1
                        a=0
                        asd=""
                        b=0
                        szx=""
                        asf2="0b"
                        while b<1790:
                            m+=[-1]
                            b=b+1
                        k = []
                        wer=""
                        qtqweqw=""
                        numberschangenotexist = []
                        numbers = []
                       
            
                        with open(nameas, "w") as f4:
                                f4.write(s)
                        with open(nameas, "a") as f3:
                                f3.write(s)
                        with open(name, "rb") as binary_file:
                            # Read the whole file at once
                            data = binary_file.read()
                            s=str(data)
                            lenf2=len(data)
                            lenf1=len(data)
                            if lenf1<6:
                                ##print("This file is too small");
                                raise SystemExit
                            if lenf1>(2**32)-1:
                                ##print("This file is too big");
                                raise SystemExit
            
                            while assx<10:
                                qqqwz=0
                                
                                a=0
                                ass=0
                                asss=0
                                b=0
                                aaqw=""
                                aaqws=""
                                l=""
                                j=0
                                b=0
                                aq=0
                                qfl=0
                                t=0
                                h=0
                                byteb=""
                                notexist=""
                                lenf=0
                                numberschangenotexistq = []
                                numberschangenotexistqz = []
                                qwa=0
                                m = []
                                p=0
                                
                                d=1
                                a=0
                                asd=""
                                b=0
                                szx=""
                                asf2="0b"
                                while b<1790:
                                    m+=[-1]
                                    b=b+1
                                k = []
                                wer=""
                                numberschangenotexist = []
                                numbers = []
                                assa=0
                                asaaq=""
                                szxzzzas=""
                                s=""
                                blockw=4
                                blockw1=3
                                sdaa=""
                                aas=0
                                asaaq=""
                                asaaqq=""
                                asaaql=""
                                asaaqll=""
                                en=0
                                assa=0
                                assas=0
                                wer=""
                                asaaqt=""
                                countraz=countraz+1
                                ddm=0
                                wers=""
                                asaaqllw=""
                                asaaqll=""
                                qqqslls=""
                                qqqslls=""
                                asaaqlls=""
                                asaaqllsq=""
                                ww=10
                                rr1=0
                                rr12=0
                                wers=""
                                countraz=0
            
            
                                
                               
            
                               
                                with open(nameas, "ab") as f2:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    
                                    lenf1=len(data) 
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                          
                                    for byte in sda:
                                        if sda[0:1]=="1":
                                            sda=sda[1:]
                                        elif sda[0:2]=="01":
                                            sda=sda[2:]
                                        elif sda[0:3]=="001":
                                            sda=sda[3:]
                                        elif sda[0:4]=="0001":
                                            sda=sda[4:]
                                        elif sda[0:5]=="00001":
                                            sda=sda[5:]
            
                                        elif sda[0:6]=="000001":
                                            sda=sda[6:]
                                        elif sda[0:7]=="0000001":
                                            sda=sda[7:]
            
                                        elif sda[0:8]=="00000001":
                                            sda=sda[8:]
            
                                            
                                        sdalong=len(sda)
            
                                        
                                        if sda[sdalong-1:sdalong]=="1":
                                            sda=sda[:sdalong-1]
                                        elif sda[sdalong-2:sdalong]=="10":
                                            sda=sda[:sdalong-2]
                                        elif sda[sdalong-3:sdalong]=="100":
                                            sda=sda[:sdalong-3]
                                        elif sda[sdalong-4:sdalong]=="1000":
                                            sda=sda[:sdalong-4]
                                        elif sda[sdalong-5:sdalong]=="10000":
                                            sda=sda[:sdalong-5]
                                        elif sda[sdalong-6:sdalong]=="100000":
                                            sda=sda[:sdalong-6]
            
                                        elif sda[sdalong-7:sdalong]=="1000000":
                                            sda=sda[:sdalong-7]
            
                                        elif sda[sdalong-8:sdalong]=="10000000":
                                            sda=sda[:sdalong-8]
            
                                            
                                        sdad=len(sda)
                                        
                                        eo=0
                                        el=0
                                        
                                        while eo<sdad:
                                            wers=""
                                            
                                            
                                            el=eo
                                            eo=eo+2523105
                                            takebitsize=sda[el:eo]
                                            xssd=len(takebitsize)
                                            el=eo-2523105
                                            eo=eo-2523105
                                            if xssd<=2523104:
                                                wer=wer+takebitsize
                                                   
                                                n = int(wer, 2)
                                        
                                                qqwslenf=len(wer)
                                                qqwslenf=(qqwslenf/8)*2
                                                qqwslenf=str(qqwslenf)
                                                qqwslenf="%0"+qqwslenf+"x"
                                             
                                                jl=binascii.unhexlify(qqwslenf % n)
                                                sssssw=len(jl)
                                                data=jl
                                                qqqwz=qqqwz+1
                                                szxzzza=""
                                                szxzs=""
                                        
                                                blockw=4
                                                blockw1=3
                                    
                                                    #print(sssssw)
                                            
                                                wer=""
                                       
                                                assx=10
                                        
                                                f2.write(jl)
                                                raise SystemExit
                                                  
                                            el=eo
                                            eo=eo+14
                                            takebit2=sda[el:eo]
                                            takebitdw2=int(takebit2, 2)
                                            
                                            el=eo
                                            eo=eo+2523092
                                            takebit=sda[el:eo]
             
                                            takebitdw=int(takebit, 2)
                                            sw=0
                                            numbertc=takebitdw
                                            
                                               
                                            while sw<180222:
                                                    
                                                numbertc3=numbertc%16383
                                                numbertc1=numbertc//16383
                                                numbertc2=int(numbertc1)
                                                    
                                                    
                                                if takebitdw2==numbertc3:
                                                    numbertc3=16383
                                                        #print(takebitdw2)
                                                       # print(numbertc3)
                                                        
                                                    
                                                szxzzz=""
                                                szxzzz=bin(numbertc3)[2:]
                                                dd=len(szxzzz)
                                                xc=14-dd%14
                                                z=0
                                                if xc!=0 and dd!=14:
                                                    while z<xc:
                                                        szxzzz="0"+szxzzz
                                                        z=z+1
                                                wers=wers+szxzzz
                                                    
                                                numbertc=numbertc2
                                                sw=sw+1
                                                    #print(sw)
                                                
                                            ddr=len(wers)
                                            
                                            sw=0
                                            el1=2523108
                                            eo1=2523108
                                           
                                            while sw<180222:
                                                    
                                                el1=eo1
                                                eo1=eo1-14
                                                takebit=wers[eo1:el1]
                                                    
                                                wer=wer+takebit
                                                sw=sw+1
                                                   
                                            wers=""    
                                           
                                    lenf=len(wer)
                                    xc=8-lenf%8
                                    z=0
                                    if xc!=0 and xc!=8:
                                        if xc!=8:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                    wer=wer+szx
                                    n = int(wer, 2)
                                    
                                    qqwslenf=len(wer)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                                        
                                       
                                                    
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    data=jl
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                   
                                    
                                    blockw=4
                                    blockw1=3
                                
                                    #print(sssssw)
                                        
                                    wer=""
                                    
                      
                                    assx=10
                                    
                                    f2.write(jl)
                                    x2 = time()
                                    x3 = x2-x
                                    return print(x3) 

    
    def Areac2(self):
                    if namez=="c2":
                        x=0
                        x1=0
                        x2=0
                        x = time()
                        name = input("What is name of file? ")
                        zzaax=""
                        szxzzzas=""
                        asaaq=""
                        assa=0
                        adwll1=0
                        ddf=0
                        cvz31=0
                        rw=0
                        qqw1q=""
                        lenfzzz=0
                        fffgjv=""
                        fffgjv1=""
                        zzaax1=""
                        qqqs=0
                        a=0
                        blockw=5
                        blockw1=4
                        cvb=0
                        aqw1=0
                        zsaqq=""
                        qqqwz=0
                        assx=0
                        ass=0
                        asss=0
                        b=0
                        aaqw=""
                        aaqws=""
                        l=""
                        j=0
                        b=0
                        aq=0
                        qfl=0
                        t=0
                        h=0
                        byteb=""
                        notexist=""
                        lenf=0
                        numberschangenotexistq = []
                        numberschangenotexistqz = []
                        qwa=0
                        add=0
                        m = []
                        p=0
                        namea=""
                        d=1
                        a=0
                        asd=""
                        b=0
                        szx=""
                        asf2="0b"
                        while b<1790:
                            m+=[-1]
                            b=b+1
                        k = []
                        wer=""
                        qtqweqw=""
                        numberschangenotexist = []
                        numbers = []
                        
                        block=180222
                        blockw=180221
                        blockw1=16384
                        virationc=16383
                        bitc=14
                        a=0
                        qfl=0
                        h=0
                        lenf1=0
                        byteb=""
                        notexist=""
                        lenf=0
                        numberschangenotexistq = []
                        qwa=0
                        z=0
                        m = []
                        p=0
                        asd=""
                        b=0
                        szx=""
                        asf2="0b"
                        while b<blockw1:
                            m+=[-1]
                            b=b+1
                        k = []
                        wer=""
                        numberschangenotexist = []
                        numbers = []
                            
                        
                        namea=name+".bin.bin"
                        namem=name+"/"
            
                        nameas=name
                        nac=len(nameas)
            
                        s=""
                        qwt=""
                        sda=""
                        ert=0
                        aqwer=0
                        aqwq=0
                        aqwers=0
                        qwaw=""
                        qwaw1=""
                        xx=0
                        xx3=0
                        with open(namea, "w") as f4:
                            f4.write(s)
                        with open(namea, "a") as f3:
                            f3.write(s)
                        with open(name, "rb") as binary_file:
                            data = binary_file.read()
                            lenf1=len(data)
                            if lenf1<400000:
                                print("This file is too small");
                                raise SystemExit
                            s=str(data)
                            lenf=len(data)
                        sda=bin(int(binascii.hexlify(data),16))[2:]
                        szx=""
                        lenf=len(sda)
                        xc=8-lenf%8
                        z=0
                        if xc!=0:
                            if xc!=8:
                                while z<xc:
                                    szx="0"+szx
                                    z=z+1
                        sda=szx+sda     
                        lenf=len(sda)
                        szx=""
            
                        for byte in sda:
                            aqwer=aqwer+1
                            aqwers=aqwers+1
                            qwaw=qwaw+byte
                            qwaw1=qwaw1+byte
                            
                                    
                            if aqwer<=bitc:
                                qwt=qwt+byte
                            if aqwer==bitc:
                                qwaw1=""
                                xx3=xx3+1
                                aqwq=int(qwt,2)
                                qwt=""
                                a=a+1
                                h=h+1  
                            av=bin(aqwq)
                            if a<=block and aqwer==bitc:
                                aqwer=0
                                m[aqwq] = aqwq
                                numbers.append(aqwq)  
                            if a == block:
                                
                                p=0
                                while p<blockw1:
                                    if p!=m[p]:
                                        k.append(p)     
                                    p=p+1
                                lenfg=len(k)
                                
                                if lenfg==0:
                                    xx=0
                                    raise SystemExit
                                if lenfg>0:
                                    acvb=lenfg-1
                                    ss=0
                                    ww=0
                                   
                                    acvb=lenfg-1
                                    notexist=k[0]
                                    
                                   
                                    
                                    if notexist>16383 or notexist<0:
                                        raise SystemExit
                                        
                                        
                                        xx=0
                                       
                                    else:
                                        xx=1
                                        szx=bin(notexist)[2:]
                                        lenf=len(szx)
                                        
                                        xc=14-lenf
                                            
                                        z=0
                                        if xc!=0 and lenf!=14:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                        takebitdw2=int(szx, 2)
                                        
                                        szxw1=""
                                        szxw1=szx
                                        
                                        lenf=len(szx)
                                       
                                        szx=""  
                                        if lenfg==0:
                                            raise SystemExit
                                b=-1
                                kl=blockw+1
                                bnkw=16383**(kl)
                                
                                
                                
                                cb=0        
                                er=-1
                                ghj=0
                                ghjd=1
                                bnk=1
                                p=0
                                cvz=0
                                if xx==1:
                                    
                                    for p in range(blockw+1):
                                        if lenfg>0:
                                            if 16383!=byteb:
                                                byteb=numbers[p]
                                                
                                                ghj=byteb
                                            if 16383==byteb:
                                                byteb=notexist
                                                
                                                ghj=byteb
                                                #print(ghj)
                                                #os.system("pause")
                                        qfl=qfl+1
                                        ghjd=ghj
                                        bnk=1
                                        
                                        bnkd=1        
                                        kl=kl-1
                                                
                                                
                                                
                                                  
                                        if lenfg>0:
                                                    
                                            bnkw=bnkw//16383
                                            #print(bnkw)
                                            #os.system("pause")
                                           
                                            
                                        
                                                        
                                                
            
                                            ghjd=0
                                            ghjd=ghj*bnkw
                                            #print(ghj)
                                                    
                                        cvz=cvz+ghjd
                                                
                                    
                                    bnkw=1023**(kl)
                                    
                                    szx=bin(cvz)[2:]
                                    cvz=0
                                    lenf=len(szx)
                                    
                                    if lenfg>0:
                                        xc=2523092-lenf
                                        z=0
                                        if xc!=0 and lenf!=2523092:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                        
                                        if xx==1:  
                                            wer=wer+szxw1+szx
                                            szxw1=""
                                       
                                            
                                        
            
                                    
                                        lenf=len(szx)
                                        
                                        szx=""
                                
                                
                                        
                                qwaw=""
                                
                                a=0
                                numberschangenotexist = []    
                                del k[:]     
                                del numbers[:]
                                m = []
                                b=0
                                while b<blockw1:
                                    m+=[-1]
                                    b=b+1
                                b=0
                                        
                        a=0
            
                        wer=wer+qwaw
                        qwaw=""
            
            
                        wer="1"+wer+"1"
                        lenf=len(wer)
                        xc=8-lenf%8
                        z=0
                        if xc!=0:
                            if xc!=8:
                                while z<xc:
                                    szx="0"+szx
                                    z=z+1
                        wer=wer+szx
                        lenf=len(szx)                      
                        szx=""        
                        wer="0b"+wer
                        n = int(wer, 2)
                        jl=binascii.unhexlify('%x' % n)
                        with open(namea, "ab") as f2ww:             
                            f2ww.write(jl)
                            x2 = time()
                            x3 = x2-x
                            return print(x3)
                   


d=compression()

xwc3=d.Areacu2()
print(xwc3)

xwc2=d.Areac2()
print(xwc2)