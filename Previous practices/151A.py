n,k,l,c,d,p,nl,np=map(int,input().split())
m=[]
m.append(int(k*l/n/nl))
m.append(int(c*d/n))
m.append(int(p/n/np))
print(min(m))