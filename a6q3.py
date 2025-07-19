t=[1,2,3,4,5,6]
A=[465,233,632,365,334,248]
r=0.045
n=4
p=[]
for i in range(len(t)):
    pv=A[i]/(1+r/n)**(n*t[i])
    p.append(pv) 
print(f'Present value of the investment: {sum(p)}')