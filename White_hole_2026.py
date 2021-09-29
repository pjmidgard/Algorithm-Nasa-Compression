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
                                        ei5=19

                                        eie4=0
                                        eie5=4

                                        eit4=0
                                        eit5=2

                                        eig4=0
                                        eig5=1
                                        
                                        Spin=0
                                        sda3=sda2
                                        ei5=6
                                        block3=0
                                        Colaider3=""
                                        sda3c=""

                                        sda3=sda3[40:]
                                        lenf5=len(sda3)

                                        Spin3=0

                                        Spin2=0

                                        while ei5<=lenf5:
                                                            Slot_16=sda3[ei4:ei4+16]#Slot 16
                                                            Slot_4_bits=sda3[ei4:ei4+4]#Slot 4
                                                            Slot_2_bits=sda3[ei4:ei4+2]#Slot 2
                                                            Slot_1a_bits=sda3[ei4:ei4+3]#Slot a 1100
                                                            Slot_1b_bits=sda3[ei4:ei4+6]#Slot a 1101
                                                            Slot_1c_bits=sda3[ei4:ei4+9]#Slot a 1110
                                                            Slot_1d_bits=sda3[ei4:ei4+13]#Slot a 1111
                                                            e4=sda3[ei4:ei5]
                                                            e4a=sda3[ei4:ei5]
                                                            e4h=sda3c[eig4:eig5]
                                                        
                                                            yu=len(e4)

                                                            if Spin==0:
                                                                eig4=eig4+1
                                                                eig5=eig5+1
                                                                
                                                                if e4h=="0":
                                                                    ei4=ei4+1
                                                                    ei5=ei5+1
                                                                   
                                                                    Spin=1

                                                                if e4h=="1":
                                                                    ei4=ei4-1
                                                                    ei5=ei5-1
                                                                    
                                                                    if Slot_2_bits=="10":
                                                                        Spin=2
                                                                        ei4=ei4+2
                                                                        ei5=ei5+2

                                                                    if e4t=="11":
                                                                        
                                                                        if Slot_4_bits=="1100" and Spin2==0:
                                                                            Spin2=1
                                                                            Spin=3

                                                                        if Slot_4_bits=="1101" and Spin2==0:
                                                                            Spin=4
                                                                            Spin2=1

                                                                        if Slot_4_bits=="1110" and Spin2==0:
                                                                            Spin=5
                                                                            Spin2=1

                                                                        if Slot_4_bits=="1111" and Spin2==0:
                                                                            Spin=6
                                                                            Spin2=1

                                                            # Spin: of varation corridors

                                                            if Spin2==1:
                                                                ei4=ei4+4
                                                                ei5=ei5+4

    
                                                                f = open("PI_10M.txt", "r")
                                                                PI=f.read()

                                                                block3 = int(e4, 2) # Take block of the file
                                                        
                                                           
                                                                szx=""

                                                            
                                                                block3=str(block3)

                                                                block=len(block3)
                                                           
                                                                PI_take=str(PI)

                                                                Spin2=0
                                                                
                                                            if Spin==1 and Spin2==0:
                                                                sda4=sda4+e4
                                                                Spin=0

                                                            if Spin==2 and Spin2==0:
                                                                #Slot_16
                                                                block3g = int(Slot_16, 2)
                                                                
                                                                PI_take_read=PI_take[block3g:block3g+5]
                                                                Colaider3=PI_take_read

                                                                Spin3=2

                                                                ei4=ei4+16
                                                                ei5=ei5+16
                                                                Spin=0

                                                            if Spin==3 and Spin2==0:
                                                                #Slot_1a_bits

                                                                block3g = int(Slot_1a_bits, 2)

                                                                PI_take_read=PI_take[block3g:block3g+1]
                                                                Colaider3=PI_take_read

                                                                Spin3=2

                                                                
                                                                ei4=ei4+3
                                                                ei5=ei5+3
                                                                Spin=0

                                                            if Spin==4 and Spin2==0:
                                                                #Slot_1b_bits

                                                                block3g = int(Slot_1b_bits, 2)
                                                                
                                                                PI_take_read=PI_take[block3g:block3g+5]
                                                                Colaider3=PI_take_read

                                                                Spin3=2

                                                                
                                                                ei4=ei4+6
                                                                ei5=ei5+6
                                                                Spin=0

                                                            if Spin==5 and Spin2==0:
                                                                #Slot_1c_bits

                                                                block3g = int(Slot_1c_bits, 2)
                                                                
                                                                PI_take_read=PI_take[block3g:block3g+5]
                                                                Colaider3=PI_take_read

                                                                Spin3=2
                                                                
                                                                ei4=ei4+9
                                                                ei5=ei5+9
                                                                Spin=0

                                                            
                                                            if Spin==6 and Spin2==0:
                                                                #Slot_1d_bits

                                                                block3g = int(Slot_1d_bits, 2)
                                                                
                                                                PI_take_read=PI_take[block3g:block3g+5]
                                                                Colaider3=PI_take_read

                                                                Spin3=2
                                                                
                                                                ei4=ei4+13
                                                                ei5=ei5+13
                                                                Spin=0

                                                            if Spin3==2:

                                                                szx=""
                                            
                                                                Colaider3=bin(block3)[2:]
                                                                lenf=len(Colaider3)
                                                                
                                                                xc2=lenf5-ei5
                                                                if xc2<=19:

                                                                    xc=xc2-lenf%xc2
                                                                    z=0
                                                                    if xc!=0:
                                                                        if xc!=xc2:
                                                                            while z<xc:
                                                                                szx="0"+szx
                                                                                z=z+1

                                                                else:
                                                                    xc=19-lenf%19
                                                                    z=0
                                                                    if xc!=0:
                                                                        if xc!=19:
                                                                            while z<xc:
                                                                                szx="0"+szx
                                                                                z=z+1

                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+Colaider3
                                                                Spin3=0

                                                                              
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
                                                sda3=sda2
                                                lenf6=len(sda3)
                                                ei4=0
                                                ei5=19
                                                block3=0
                                                Colaider3=""
                                                block2=0
                                                block3=0

                                                f = open("PI_10M.txt", "r")
                                                PI=f.read()
                                                
                                                while ei5<lenf5*8+19:
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
                                                            lenf=len(PI_take_long)
                                                            
                                                            Colaider3=bin(xe)[2:]
                                                            lenf_bits=len(PI_take_long)

                                                            if xe==-1:

                                                
                                                                sda4=sda4+"0"+e4
                                                               

                                                            elif lenf<=1 and block==1 and lenf_bits<=3:
                                                            
                                                                xc=3-lenf%3
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=3 and xc!=0:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                               
                                                                sda4=sda4+"1100"+Colaider3
                                                                
                                                                

                                                            elif lenf<=2 and block==2 and lenf_bits<=6:
                                                            
                                                                xc=6-lenf%6
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=6 and xc!=0:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"1101"+Colaider3
                                                               
                                                                
                                                             
                                                            
                                                            elif lenf<=3 and block==3 and lenf_bits<=9:
                                                            
                                                                xc=9-lenf%9
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=9 and xc!=0:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"1110"+Colaider3
                                                                
                                                               

                                                            elif lenf<=4 and block==4 and lenf_bits<=13:
                                                            
                                                                xc=13-lenf%13
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=13 and xc!=0:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"1111"+Colaider3
                                                               

                                                            elif lenf<=5 and block==5 and lenf_bits<=16:
                                                            
                                                                xc=16-lenf%16
                                                                z=0
                                                                if xc!=0:
                                                                    if xc!=16 and xc!=0:
                                                                        while z<xc:
                                                                            szx="0"+szx
                                                                            z=z+1
                                                                                        
                                                                Colaider3=szx+Colaider3
                                                                sda4=sda4+"10"+Colaider3
                                                                
                                                             
                                                            elif lenf>=6 and block>=6:
                                                                 
                                                                sda4=sda4+"0"+e4
                                                            
                                                            ei4=ei4+19
                                                            ei5=ei5+19
                                        
                                    szx=""

                                     
                                    sda6=""

                                    sda4f=len(sda4)
                                    
                                    Colaider3=bin(sda4f)[2:]
                                    lenf=len(Colaider3)
                                    xc=40-lenf%40
                                    z=0
                                    if xc!=0:
                                        if xc!=40 and xc!=0:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                                
                                    Colaider3=szx+Colaider3
   							                                   
                                    sda6=Colaider3+sda4
                                                         
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
