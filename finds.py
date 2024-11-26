a=""
ff=input("give a .cs csharp file to find flux? ")
f1=open(ff,"r")
a=f1.read()
f1.close()
c=a
tTrue=True
count=0
list1=[]
b=0
d=0
e=0
lens=len(a)
while tTrue:
    b=a.find("{",count)
    d=a.find("}",count)
    if b>-1:
       e=b
       if d>-1:
          if d<b:
              list1=list1+[d]
              if d<lens:
                  count=d+1
              else:
                  tTrue=False 
          else:
              list1=list1+[b]
              if b<lens:
                  count=b+1
       else:
           list1=list1+[b]
           if b<lens:
                  count=b+1
           else:
               tTrue=False
    else:
        if d>-1:
          
           list1=list1+[d]
           if d<lens:
              count=d+1
           else:
              tTrue=False 
        else:
            tTrue=False

back=0
calls=0
fluxo="main:\n"
chamber=0
chars=0
tTrue=True
for n in range(len(list1)):    
    if a[list1[n]]=="}":
        tTrue=True
        nn=n
        chamber-=1
        chars=chamber
        
        c1=list1[0]
        while tTrue:
            nn-=1
            if a[list1[nn]]=="{":
                chars-=1
                if chars<1:
                    c1=list1[nn]+1
                    tTrue=False
            
            if nn<1:
                tTrue=False
        c2=list1[n]
        bh=a[c1:c2].strip()
        print(bh)
        print("---------------")
        calls+=1
    else:
        chamber+=1
