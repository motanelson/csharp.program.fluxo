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
for n in list1:
    if a[n]=="}":
        fluxo=fluxo+"call calls"+str(calls)+":\n" 
        c1=back
        c2=n
        print("---------------\ncall"+str(calls)+":\n")
        bh=a[c1:c2].strip()
        print(bh)
        print("ret\n---------------")
        calls+=1
    back=n
print(fluxo)