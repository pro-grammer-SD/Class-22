t = (1,0,0,1,1,0)
r = 0
s = 0

for n in t:
    if n == 1:
        r += 1
    
    else:
        s += 1
        
if r > s:
    print("Rainy weather will occur!")

elif s > r:
    print("Sunny weather will occur!")
    
else:
    print("There is equal chance!")