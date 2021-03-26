def solution(N):
    len=0
    mx =0
    last=0
    while (N>0):
        d = N%2
        if (d == 0):
            if (last == 1):
                
                len = 1
            else:
                if len > 0:
                    len = len+1
                    
        else:
            mx = max (mx, len)
            len=0
        last = d
        N = N//2
    return mx

for n in [9,529,20,32,1041,15]:
    print(n,' ',solution(n))
    
for n in [1,2,147,483,647]:
    print(n,' ',solution(n))
    
    
        