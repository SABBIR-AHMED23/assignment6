import math
t=[1,2,3,4,5]
A=[225,215,250,225,205]
B=[220,225,250,250,210]
r=0.0433
# For investment A
p=[]
for i in range(len(t)):
    pv=A[i]/math.exp(r*t[i])
    p.append(pv)
print(f'Present Value of Investment A: {sum(p)}')    

# For investment B
q=[]
for i in range(len(t)):
    pv=B[i]/math.exp(r*t[i])
    q.append(pv)
print(f'Present Value of Investment B: {sum(q)}') 
if sum(p)>sum(q):
    print('Investment A is preferable.')
else:
    print('Investment B is preferable.')