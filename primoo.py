d,k=map(int,input().split())
for i in range(d+1,k,1):
	k+=1
	if d%i==0:
		break
	else:
		print(i)
	    
