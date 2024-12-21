num = int(input("Enter Number"))
t = num 
numlen = 0 
while t > 0:
    numlen = numlen + 1
    t = int( t / 10)
if numlen >= 4:
    numlen = int(numlen/2)
    c = 0
    while num > 0 :
        r = num % 10 
        if c == numlen:
            midone = r
        elif c == (numlen - 1):
            midtwo = r
        num = int(num / 10)
        c = c + 1
    product = midone * midtwo
    print("Prouct of middle digits", product)
else:
    print("Its not a 4 or more digit number") 
    