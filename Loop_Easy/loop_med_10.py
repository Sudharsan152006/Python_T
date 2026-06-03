p,d,m = map(int,input().split())

for i in range(m):
    p= p-(p*d/100)
    
    
print("%.2f"%p)
