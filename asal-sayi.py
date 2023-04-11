x = int(input())
count = 0
for i in range(1,x+1) :
    if x%i ==0 : count +=1
    else: 
        count +=0
if count < 3 :
    print(f'{x} sayisi asal')
else:
     print(f'{x} sayisi asal degil ')
