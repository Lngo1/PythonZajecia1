while True:
    s=input("wyberz znak(+,-,*,/,%,**):")
    if s=="0":
        break
    if s in ('+','-','*','/','%','**'):
        x=float(input("x="))
        y=float(input("y="))
        if s=='+':
            print(x+y)
        elif s=='-':
            print(x-y)
        elif s=='*':
            print(x*y)
        elif s=='/':
            if y !=0:
                print(x/y)
            else:
                print('nie mozna podelicz na 0')    
        elif s=='%':
            print(x%y)
        elif s=='**':
            print(x**y)
