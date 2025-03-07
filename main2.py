wtuple = (1,2,3,3,2,1)
w = "".join(reversed(str(wtuple)))
w2 = w.replace("(","").replace(")","").replace(",","")
w3 = w = "".join(reversed(w2))
if w2 == w3:
    print("hurray")
else:
    print("bruh")