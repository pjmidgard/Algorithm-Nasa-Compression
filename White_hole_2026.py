from time import time
cvf=0
import os
import binascii

#import mpmath as m
#m.mp.dps = 100000
#PI=4 * m.atan(1)

Circle_times=0
END_working=0
lenf=0
namea=""
szx=""
wer=""

namez = input("c for compress or e for extract? ")
#@Author Jurijus pacalovas
class compression:
                
    def cryptograpy_compression(self):
                
                self.name = "Written: Jurijus pacalovas Date: 16/09/2021 14:23"
                
                if namez=="c" or namez=="e":
                    if namez=="c":
                        i=1
                    if namez=="e":
                        i=2

                     
                    sda4=""
                    sda5=""
                    sda6=""
                    e4a=""
                    e4b=""
                    ei8=""
                        
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)

                    if i==2:
                        if nameas[nac-4:nac]!=".bin":
                             print("Program close because this is file is not .bin")
                             raise SystemExit
                        
                        nameas=name[:nac-4]
                        nac=len(nameas)
                    
                    if i==1:
                       
                        nameas=name+".bin"
                    
                    nac=len(nameas)
                    
                    Circle_times3=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                    e2=0
                    e3=1
                    e4=""
                    ei4=0
                    ei5=7
                    
                    
                    e4=""
                    
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    block=1
                    block2=0
                    block3=0
                    
                    

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        END_working=0
                        Circle_times=0
                        Circle_times2=0


                       
                        while END_working<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            Circle_times3=Circle_times3+1

                            with open(nameas, "ab") as f2:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if Circle_times3==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)
                                
                                    
                                     
                                block2=0
                                if i==2:

                                    
                                    sda2=sda2[1:]
                                    lenf5=len(sda3)
                                    g=1


                                    if g==1:

                                        if sda2[lenf5-8:lenf5]=="10000000":

                                            sda2=sda2[:lenf5-8]

                                        elif sda2[lenf5-7:lenf5]=="1000000":

                                            sda2=sda2[:lenf5-7]

                                        elif sda2[lenf5-6:lenf5]=="100000":

                                            sda2=sda2[:lenf5-6]

                                        elif sda2[lenf5-5:lenf5]=="10000":

                                            sda2=sda2[:lenf5-5]


                                        elif sda2[lenf5-3:lenf5]=="100":

                                            sda2=sda2[:lenf5-3]

                                        elif sda2[lenf5-2:lenf5]=="10":

                                            sda2=sda2[:lenf5-2]

                                        elif sda2[lenf5-1:lenf5]=="1":

                                            sda2=sda2[:lenf5-1]

                                        
                                        lenf5=len(sda2)
                                        
                                        block2=0
                                        ei4=0
                                        ei5=6

                                        eig4=0
                                        eig5=1
                                        
                                        Spin=0
                                        sda3=sda2
                                        ei5=6
                                        block3=0
                                        Colaider3=""
                                        sda3c=""

                                        e4l=sda3[ei4:ei4+32]
                                        e4l=int(e4l, 2)

                                        sda3=sda3[32:]

                                        sda3c=sda3[:e4l]
                                        sda3=sda3[e4l:]
                                        Spin2=0

                                        

                                        
        
                                        while ei5<lenf5+32:
                                                            e4b=sda3[ei4:ei4+6]
                                                            e4=sda3[ei4:ei5]
                                                            e4a=sda3[ei4:ei5]
                                                            e4h=sda3c[eig4:eig5]
                                                          
                                                            yu=len(e4)

                                                            szx=""

                                                            Colaider3=bin(block3)[2:]
                                                            lenf=len(Colaider3)
                                                             
                                                            xc=6-lenf%6
                                                            z=0
                                                            if xc!=0:
                                                                if xc!=6:
                                                                    while z<xc:
                                                                        szx="0"+szx
                                                                        z=z+1
                                                                            
                                                            Colaider3=szx+Colaider3
                                                           
                                                            if block2==16:
                                                                
                                                                
                                                                block2=0
                                                                Specktr=0
                                                                Spin=0
                                                                
                                                        
                                                                block3=0
                                                                Spin2=0
                                                            
                                                            if Spin2==1 and block2==15:
                                                                Specktr=1
                                                            
                                                            
                                                                sda4=sda4+Colaider3
                                                                
                                                              

                                                            if Spin2==0:
                                                                ei4=ei4+1
                                                                ei5=ei5+1
                                                                if e4h=="1":
                                                                    Spin2=1
                                                                    block2=0
                                                                    block3=0
                                                                    Spin=1
                                                                    Spin2=0

                                                                if e4h=="0":
                                                                    
                                                                    sda4=sda4+e4
                                                                    block2=block2+1
                                                                    block3=block3+1
                                                                    
                                                            else:
                                                                sda4=sda4+e4
                                                                block2=block2+1
                                                                block3=block3+1

                                                            
                                                            
                                                            ei4=ei4+6
                                                            ei5=ei5+6

                                    e4=""
                                    e4a=""
                                    e4b=""
                                    block2=0
                                    sda5=""
                                    cvf1=1

                                   
                                lenf6=len(sda4)
                                lenf8=len(sda2)
                                   
                                                                
                               
                                e2=e2+1
                                e3=e3+1

                                e4=""

                              
                          
                                
                                cvf1=1
                                if cvf1==1:
                                    
                                    if i==1:
                                                Spin=0
                                                sda3=sda2[:1000*8]
                                                lenf6=len(sda3)
                                                ei4=0
                                                ei5=32
                                                block3=0
                                                Colaider3=""
                                                block2=0
                                                block3=0

                                                f = open("PI_10M.txt", "r")
                                                PI=f.read()
                                                
                                                while ei5<lenf6+32:
                                                            e4b=sda3[ei4:ei4+6]
                                                            e4=sda3[ei4:ei5]
                                                            e4a=sda3[ei4:ei5]
                                                            yu=len(e4)

                                                           
                                                            block3 = int(e4, 2) # Take block of the file
                                                        
                                                           
                                                            szx=""

                                                            
                                                            block3=str(block3)

                                                            block=len(block3)
                                                           
                                                            PI_take=str(PI)
                                                            

                                                            xe = PI_take.find(block3)

                                                            PI_take_long=str(xe)
                                                           
                                                            
                                                            Colaider3=bin(xe)[2:]

                                                            lenf=len(Colaider3)
                                                            

                                                            if lenf==0 or PI_take_long=="-1":

                                                
                                                                sda4=sda4+"0"+e4
                                                                

                                                            elif lenf!=0 and block==1 and PI_take_long!="-1":
                                                            
                                                                xc=3-lenf%3
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=3:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                               
                                                                sda4=sda4+"11000"+Colaider3
                                                                
                                                                

                                                            elif lenf!=0 and block==2 and PI_take_long!="-1":
                                                            
                                                                xc=6-lenf%6
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=6:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"11001"+Colaider3
                                                                
                                                             
                                                            
                                                            elif lenf!=0 and block==3 and PI_take_long!="-1":
                                                            
                                                                xc=9-lenf%9
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=9:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"11010"+Colaider3
                                                               

                                                            elif lenf!=0 and block==4 and PI_take_long!="-1":
                                                            
                                                                xc=13-lenf%13
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=13:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"11011"+Colaider3
                                                                


                                                            elif lenf!=0 and block==5 and PI_take_long!="-1":
                                                            
                                                                xc=16-lenf%16
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=16:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"11100"+Colaider3
                                                               

                                                            elif lenf!=0 and block==6 and PI_take_long!="-1":
                                                            
                                                                xc=19-lenf%19
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=19:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"11101"+Colaider3
                                                                


                                                            elif lenf!=0 and block==7 and PI_take_long!="-1":
                                                            
                                                                xc=24-lenf%24
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=19:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"11110"+Colaider3
                                                                

                                                            
                                                            elif lenf!=0 and block==8 and PI_take_long!="-1":
                                                            
                                                                xc=26-lenf%26
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=26:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"11111"+Colaider3
                                                                

                                                            elif lenf!=0 and block==9 and PI_take_long!="-1":
                                                            
                                                                xc=29-lenf%29
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=29:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"10"+Colaider3
                                                           
                                                            else:
                                                                 
                                                                sda4=sda4+"0"+e4

                                                                
                                                            ei4=ei4+32
                                                            ei5=ei5+32
                                        
                                    szx=""

                                     
                                    sda6=""

                                    sda4f=len(sda4)
                                    
                                    Colaider3=bin(sda4f)[2:]
                                    lenf=len(Colaider3)
                                    xc=13-lenf%13
                                    z=0
                                    if xc!=0:
                                        if xc!=13:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                                
                                    Colaider3=szx+Colaider3
   							                                   
                                    sda6=Colaider3+sda4+sda2[1000*8:]
                                                         
                                    block2=0
                                    Spin=1
                                    Spinh=0              
                                    block2=0
                                

                                    
                                    e4=""
                                    e4a=""
                                    e4b=""
                                    block2=0
                                    sda5=""
                                     
                                    cvf1=1
                                                
                                    if cvf1==1:
                                                    if i==2:
                                                        wer=""
                                                        szx=""
                                                        wer=sda4

                                                    if i==1:
                                                        wer=""
                                                        wer=sda6
                                                        sda4=""
                                                        szx=""

                                                        wer="0"+wer+"1"
                                                        lenf=len(wer)
                                                        
                                                        xc=8-lenf%8
                                                        z=0
                                                        if xc!=0:
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
                                                    
                                                    Circle_times=Circle_times+1
                                                    szxzzza=""
                                                    szxzs=""
                                                    sda2=sda6
                                                    
                                                    Circle_times2=Circle_times2+1
                                                    
                                                    
                                                    if Circle_times2==1:
                                                        END_working=10 
                                                    if END_working==10:        
                                              
                                                        f2.write(jl)
                                                        x2 = time()
                                                        x3=x2-x
                                                        return print(x3)

d=compression()

xw=d.cryptograpy_compression()
print(xw)
